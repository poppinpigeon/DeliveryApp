import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDcvUBYw6-GJ4CsNZp0s2K0lCuxn1t5WvU",
    "authDomain": "delivery-project-53cf8.firebaseapp.com",
    "databaseURL": "https://delivery-project-53cf8-default-rtdb.firebaseio.com",
    "projectId": "delivery-project-53cf8",
    "storageBucket": "delivery-project-53cf8.appspot.com",
    "messagingSenderId": "496610742801",
    "appId": "1:496610742801:web:2fae127ebafea3bb51d7b0"
    }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def addOrder(user_info):
    db.child("Orders").push(user_info)