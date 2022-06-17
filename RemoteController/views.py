from django.shortcuts import render
from django.views import View
import pyrebase

from .firebase_credentials import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

class MainView(View):
    def get(self, request):
        devices = db.child("lab").get().val()
        ctx = {'devices':devices}
        return render(request, 'RemoteController/index.html', ctx)