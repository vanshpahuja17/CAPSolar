from django.shortcuts import render, redirect
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
    sensor = database.child('Realtime').child('0').get().val()
    sensor1 = database.child('Realtime').child('1').get().val()
    print(sensor)
    return render(request, 'app/dashboard.html')