from django.shortcuts import render, redirect
from .firebase_config import *
from django.contrib import messages

import pyrebase

config = {
    'apiKey': "AIzaSyC9Su0Qp87w52JnFegOQJLPNAC5qmNepik",
    'authDomain': "bigproject-d6846.firebaseapp.com",
    'databaseURL': "https://bigproject-d6846-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "bigproject-d6846",
    'storageBucket': "bigproject-d6846.appspot.com",
    'messagingSenderId': "962134580824",
    'appId': "1:962134580824:web:87e73c1b8dd970f9af742d",
    'measurementId': "G-L6ZXTYCE66"
}
fb = pyrebase.initialize_app(config)
aut = fb.auth()


# Login / Logout
def home(request):
    if request.session['uid']:
        return redirect('dashboard')
    else:
        request.session['uid'] = None
        return render(request, 'home.html')


# Logout required
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = aut.sign_in_with_email_and_password(email, password)
            request.session['uid'] = user['localId']
            return redirect("dashboard")
        except Exception as e:
            request.session['uid'] = None
            messages.info(request, "Either password or email-id is incorrect, try again.")
            return redirect("login")

    else:
        if not request.session['uid']:
            request.session['uid'] = None
            return render(request, 'login.html')
        else:
            return redirect('dashboard')


# Logout required
def register(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['Password']

        try:
            user = aut.create_user_with_email_and_password(email, password)
            return redirect("login")
        except Exception as e:
            print(e)
            messages.info(request, "Something went wrong!!")
            return redirect("register")

    else:
        if not request.session['uid']:
            return render(request, 'register.html')
        else:
            return redirect('dashboard')


# Login required
def dashboard(request):
    if request.session.get('uid'):
        return render(request, 'dashboard.html')
    else:
        return redirect("login")


# Login required
def logout(request):
    if request.session.get('uid'):
        request.session['uid'] = None
    return redirect('login')
