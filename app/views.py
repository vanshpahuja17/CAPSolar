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
    sensor = database.child('Realtime').get().val()
    sensor1 = database.child('Realtime').child('1').get().val()
    nox = []
    cox = []
    benzene = []
    solar = []
    time = []
    for i in sensor:
        benzene.append(i['Benzene'])
        cox.append(i['COx'])
        nox.append(i['NOx'])
        solar.append(i['Solar Voltage'])
        time.append(i['Timestamp'])
    return render(request, 'app/dashboard.html',{
    'nox':nox,
    'cox':cox,
    'benzene':benzene,
    'solar':solar,
    'time':time,
})