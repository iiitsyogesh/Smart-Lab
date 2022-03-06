from django.shortcuts import render
from django.views import View
from .firebase_credentials import firebaseConfig
import pyrebase

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

class MainView(View):
    def get(self, request):
        devices = db.child("user").get().val()
        ctx = {'devices':devices}
        return render(request, 'RemoteController/index.html', ctx)