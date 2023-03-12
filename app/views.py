from django.shortcuts import render, redirect
import pyrebase

config={
    "apiKey": "AIzaSyBKl2d1JSdSpEAz3ryiaBr11u5SxCgA-8c",
    "authDomain": "capsolar-5c360.firebaseapp.com",
    "databaseURL": "https://capsolar-5c360-default-rtdb.firebaseio.com",
    "projectId": "capsolar-5c360",
    "storageBucket": "capsolar-5c360.appspot.com",
    "messagingSenderId": "615977434602",
    "appId": "1:615977434602:web:1b54c635ac7d626fc20693",
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def Dashboard(request):
    sensor = database.child('NOx').child('16:15:59').get().val()
    sensor1 = database.child('NOx').child('16:16:44').get().val()
    print(sensor)
    return render(request, 'app/dashboard.html')