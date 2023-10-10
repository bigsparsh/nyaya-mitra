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


def home(request):
    try:
        if request.session['uid']:
            return redirect('dashboard')
        else:
            return render(request, 'home.html')
    except KeyError as e:
        print("Error denied: ", e)
        return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = aut.sign_in_with_email_and_password(email, password)
            request.session['uid'] = user['localId']
            return redirect('dashboard')
        except Exception as e:
            messages.info(request, "Invalid Email-ID or password")
            print('Exception: ', e)
            return redirect('login')

    else:
        try:
            if request.session['uid']:
                print('Session is active')
                return redirect('dashboard')
            else:
                raise KeyError
        except KeyError as e:
            print('Session is not active. Exception: ', e)
            return render(request, 'login.html')


def logout(request):
    try:
        if request.session['uid']:
            print('Session is active')
            request.session['uid'] = None
        return redirect('login')
    except KeyError as e:
        print('Exception occurred: ', e)
        return redirect('login')


def register(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['Password']

        try:
            user = aut.create_user_with_email_and_password(email, password)
            return redirect('login')
        except Exception as e:
            messages.info(request, "Either this Email-ID is taken or the password is less than 6 characters.")
            print('Exception: ', e)
            return redirect('register')

    else:
        try:
            if request.session['uid']:
                print('Session is active')
                return redirect('dashboard')
            else:
                raise KeyError
        except KeyError as e:
            print('Session is not active. Exception: ', e)
            return render(request, 'register.html')


def dashboard(request):
    try:
        if request.session['uid']:
            return render(request, 'dashboard.html')
        else:
            raise KeyError
    except KeyError as e:
        print("Session not active: ", e)
        return redirect('login')
