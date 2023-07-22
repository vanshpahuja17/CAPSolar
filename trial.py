import csv
import time
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("./path/serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://realtime-ef8a9-default-rtdb.firebaseio.com/'
})

ref = db.reference('Realtime')
ref2 = db.reference('Evening')
ref3 = db.reference('Afternoon')
ref5 = db.reference('Morning')
while True:
    with open('./Morning.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        ref5.set(data)
   
    with open('./Cleaned_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        ref.set(data)
 
    with open('./Evening.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        ref2.set(data)

    with open('./Afternoon.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        ref3.set(data)
    time.sleep(10)
# with open('C:/Users/Lenovo/Desktop/Firebase/Cleaned_data.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     data = [row for row in reader]



# ref.set(data)
# ref.update(data)


