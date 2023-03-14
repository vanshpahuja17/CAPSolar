from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.conf import settings
import random
from django.core.exceptions import MultipleObjectsReturned
from django.http import JsonResponse
from django.http import QueryDict
import pyrebase

config={
    "apiKey": "AIzaSyCbVaFO_NUjdKysYvm54bwgYQW4Puyfc0k",
    "authDomain": "realtime-ef8a9.firebaseapp.com",
    "databaseURL": "https://realtime-ef8a9-default-rtdb.firebaseio.com",
    "projectId": "realtime-ef8a9",
    "storageBucket": "realtime-ef8a9.appspot.com",
    "messagingSenderId": "1071615041026",
    "appId": "1:1071615041026:web:53c2b4079a9568417f111b",
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def Dashboard(request):
    sensor = database.child('Realtime').get().val()
    sensor1 = database.child('Evening').get().val()
    sensor2 = database.child('Afternoon').get().val()
    sensor3 = database.child('Morning').get().val()
    nox = []
    cox = []
    benzene = []
    solar = []
    time = []

    nox_evening = []
    cox_evening = []
    benzene_evening = []
    time_evening = []
    solar_evening = []

    nox_afternoon = []
    cox_afternoon = []
    benzene_afternoon = []
    time_afternoon = []
    solar_afternoon = []

    nox_morning = []
    cox_morning = []
    benzene_morning = []
    time_morning = []
    solar_morning = []
    benzenes = 0
    for i in sensor:
        benzene.append(i['Benzene'])
        cox.append(i['COx'])
        nox.append(i['NOx'])
        solar.append(i['Solar Voltage'])
        time.append(i['Timestamp'])
    for i in sensor1:
        benzene_evening.append(i['Benzene'])
        cox_evening.append(i['COx'])
        nox_evening.append(i['NOx'])
        solar_evening.append(i['Solar Voltage'])
        time_evening.append(i['ï»¿Timestamp'])
    for i in sensor2:
        benzene_afternoon.append(i['Benzene'])
        cox_afternoon.append(i['COx'])
        nox_afternoon.append(i['NOx'])
        solar_afternoon.append(i['Solar Voltage'])
        time_afternoon.append(i['ï»¿Timestamp'])
    for i in sensor3:
        benzene_morning.append(i['Benzene'])
        cox_morning.append(i['COx'])
        nox_morning.append(i['NOx'])
        solar_morning.append(i['Solar Voltage'])
        time_morning.append(i['ï»¿Timestamp'])
    # if request.method == "POST":
        # name = request.POST.get('lname')
        # lname = request.POST.get('lname')
    email = request.session['email']
    
        # contact = request.POST.get('contact')
    if(benzenes>=49):
        print(email)
        messages.error(request, "This value of Benzene will decrease the value of solar power.")

        send_mail(
        'Alert',
            'Dear User' +', The concentation of benzene has increased in the atmosphere, hence you may see a drop in solar power. '+'Please Click http://127.0.0.1:8000/threshold_sample/ to know more',
            '2020.vansh.pahuja@ves.ac.in',
            [email],
            fail_silently=False,
        )
    return render(request, 'app/dashboard.html',{
    'sensor':sensor,
    'nox':nox,
    'cox':cox,
    'benzene':benzene,
    'solar':solar,
    'time':time,

    'sensor1':sensor1,
    'cox_evening':cox_evening,
    'nox_evening': nox_evening,
    'benzene_evening': benzene_evening,
    'solar_evening': solar_evening,
    'time_evening': time_evening,

    'sensor2':sensor2,
    'cox_afternoon':cox_afternoon,
    'nox_afternoon': nox_afternoon,
    'benzene_afternoon': benzene_afternoon,
    'solar_afternoon': solar_afternoon,
    'time_afternoon': time_afternoon,   

    
    'sensor3':sensor3,
    'cox_morning':cox_morning,
    'nox_morning': nox_morning,
    'benzene_morning': benzene_morning,
    'solar_morning': solar_morning,
    'time_morning': time_morning,   
})

def notifications(request):
    if Notification.objects.filter(email= request.session['email']).exists():
        try:
            data = []
            data = Notification.objects.get(email= request.session['email'])
        except MultipleObjectsReturned:
            data=Notification.objects.filter(email= request.session['email']).first()
    
    else:
        return redirect('dashboard')
        messages.success("Please schedule an appointment first")
    return render(request, 'app/notifications.html',{'data':data})

    return render(request , "app/notifications.html")

def send_otp_email(otp, email):
    subject = "Verify your Email - {}".format(email)
    print(otp)
    message = "Your 4-digit OTP to verify your account is : " + str(otp) + ". Please don't share it with anyone else"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def send_psw_email(otp, email):
    subject = "Reset your Password - {}".format(email)
    print(otp)
    message = "Your 4-digit OTP to reset your password is : " + str(otp) + ". Please don't share it with anyone else"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def Register(request):
    if request.method == "POST":
        
        fnd1 = User.objects.filter(email = request.POST['email'].lower())
        # fnd2 = Company.objects.filter(email = request.POST['email'].lower())
        if len(fnd1) == 0:
            request.session['name'] = request.POST['name']
            request.session['email'] = request.POST['email'].lower()
            request.session['password'] = request.POST['password']
            # request.session['role'] = request.POST['role']
            cpswd = request.POST['confirmPassword']

            if request.session['password'] == cpswd:
                # if request.session['role'] == 'applicant':
                request.session['contact'] = request.POST['contact']
                request.session['location'] = request.POST['location']
                request.session['gender'] = request.POST['gender']

                request.session['password'] = make_password(request.POST['password'])
                request.session['otp'] = random.randint(1000,9999)
                send_otp_email(request.session['otp'], request.session['email'])
                messages.success(request, "OTP is sent to your email. Please enter it.")
                return redirect("verifyotppage")
            else:
                messages.error(request, "Password and Confirm Password do not match. Please try again")
                return redirect("register")
        else:
            messages.error(request, "User already exists. Please login")
            return redirect("login")
    else:
        return render(request, "app/auth-register-applicant.html")

def Login(request):
    if request.method == "POST":
        email = request.POST['email'].lower()
        pswd = request.POST['password']
        fnd1 = User.objects.filter(email = request.POST['email'].lower())
        # fnd2 = Company.objects.filter(email = request.POST['email'].lower())
        if len(fnd1) > 0:
            if check_password(pswd, fnd1[0].password):
                request.session['id'] = fnd1[0].id
                request.session['name'] = fnd1[0].name
                request.session['email'] = fnd1[0].email
                # request.session['role'] = fnd1[0].role
                # request.session['totalPoints'] = fnd1[0].totalPoints
                return redirect("dashboard")
            else:
                messages.error(request, "Please enter a valid password")
                return redirect("login")
        # elif len(fnd2) > 0:
        #     if fnd2[0].is_active == True:
        #         if check_password(pswd, fnd2[0].password):
        #             request.session['id'] = fnd2[0].id
        #             request.session['name'] = fnd2[0].name
        #             request.session['email'] = fnd2[0].email
        #             # request.session['role'] = fnd2[0].role
        #             return redirect("dashboard")
        #         else:
        #             messages.error(request, "Please enter a valid password")
        #             return redirect("login")
            # else:
            #     messages.error(request, "Account locked. Contact admin to unlock.")
            #     return redirect("login")
        else:
            messages.error(request, "User does not exist. Please register.")
            return redirect("register")
    else:
        return render(request, "app/login.html")
    
def Logout(request):
    if 'email' in request.session:
        # if request.session['role'] == 'applicant':
        #     del request.session['totalPoints']
        del request.session['id']
        del request.session['name']
        del request.session['email']
        # del request.session['role']
        return redirect("login")
    else:
        return redirect("login")

def VerifyOTPPage(request):
    return render(request, "app/auth-register-otp.html")

def FpEmailPage(request):
    return render(request, "app/auth-fp-email.html")

def FpOTPPage(request):
    return render(request, "app/auth-fp-otp.html")

def FpPasswordPage(request):
    return render(request, "app/auth-fp-password.html")

def VerifyOTP(request):
    if request.method == "POST":
        name = request.session['name']
        # role = request.session['role']
        email = request.session['email']
        mainotp = request.POST['otp']
        print(type(mainotp), type(request.session['otp']))
        if request.session['otp'] == int(mainotp):
            # if role == 'company':
            #     addCompany = Company.objects.create(
            #         name = name,
            #         email = email,
            #         password = request.session['password']
            #     )
            #     del request.session['password']
            #     del request.session['email']
            #     del request.session['name']
            #     del request.session['otp']
                # del request.session['role']
        
            contact = request.session['contact']
            gender = request.session['gender']
            location = request.session['location']
            applicant = User.objects.create(
                name = name,
                email = email,
                contact = contact,
                location = location,
                gender = gender,
                password = request.session['password']
            )
            del request.session['password']
            del request.session['email']
            del request.session['name']
            del request.session['contact']
            del request.session['gender']
            del request.session['location']
            del request.session['otp']
            messages.success(request, "You have Registered successfully. Login to continue.")
            return redirect("login")
        else:
            messages.error(request, "Invalid OTP. Please try again")
            return redirect("verifyotppage")

def FpEmail(request):
    if request.method == "POST":
        email = request.POST['email'].lower()
        user1 = User.objects.filter(email = email)
        # user2 = Company.objects.filter(email = email)
        if user1:
            request.session['email'] = email
            request.session['role'] = 'applicant'
            request.session['otp'] = random.randint(1000,9999)
            send_psw_email(request.session['otp'], request.session['email'])
            return redirect("fpotppage")
        # if user2:
        #     request.session['email'] = email
        #     request.session['role'] = 'company'
        #     request.session['otp'] = random.randint(1000,9999)
        #     send_psw_email(request.session['otp'], request.session['email'])
        #     return redirect("fpotppage")
        else:
            messages.error(request, "User does not exist. Please Register")
            return redirect("register")

def FpOTP(request): 
    if request.method == "POST":
        eml = request.session['email'].lower()
        mainotp = request.POST['otp']
        if request.session['otp'] == int(mainotp):
            del request.session['otp']
            return redirect("fppasswordpage")
        else:
            messages.error(request, "Invalid OTP. Please try again")
            return redirect("fpotppage")

def FpPassword(request):
    if request.method == "POST":
        fnd = User.objects.get(email = request.session['email'])
        pswd = request.POST['password']
        cpswd = request.POST['confirmPassword']
        if pswd == cpswd:
            fnd.password = make_password(pswd)
            fnd.save()
            del request.session['email']
            del request.session['role']
            messages.success(request, "Password changed successfully. Login to continue.")
            return redirect("login")
        else:
            messages.error(request, "Password and Confirm Password do not match. Please try again")
            return redirect("fppasswordpage")
        
def Threshold(request):
    if Notification.objects.filter(email= request.session['email']).exists():
        try:
            data = []
            data = Notification.objects.get(email= request.session['email'])
        except MultipleObjectsReturned:
            data=Notification.objects.filter(email= request.session['email']).first()
    
    else:
        return redirect('dashboard')
        messages.success("Please schedule an appointment first")
    return render(request, 'app/threshold_sample.html',{'data':data})

    return render(request , "app/notifications.html")