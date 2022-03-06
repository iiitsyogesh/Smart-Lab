from django.shortcuts import render
from django.views import View
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyD0TftQQlr--6pSMyUXzw5QT4pFM1kB-HM",
    'authDomain': "smart-home-16c6c.firebaseapp.com",
    'databaseURL': "https://smart-home-16c6c-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "smart-home-16c6c",
    'storageBucket': "smart-home-16c6c.appspot.com",
    'messagingSenderId': "1020150526141",
    'appId': "1:1020150526141:web:d0ef2d2dd41178838447d4"
}
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

class MainView(View):
    def get(self, request):
        devices = db.child("user").get().val()
        ctx = {'devices':devices}
        return render(request, 'RemoteController/index.html', ctx)