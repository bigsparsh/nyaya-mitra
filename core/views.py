from django.shortcuts import render, redirect
from .firebase_config import *
from django.contrib import messages
import pyrebase
from firebase_admin import credentials, firestore

fire_db = firestore.client()

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
    result = fire_db.collection('Top_Lawyers').get()
    top_lawyers = []
    for r in result:
        top_lawyers.append(r.to_dict()['path'].get().to_dict())
    try:
        if request.session['uid']:
            return redirect('dashboard')
        else:
            raise KeyError
    except KeyError as e:
        print("Error denied: ", e)
        return render(request, 'home.html', {'top_lawyers': top_lawyers})


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


def user_register(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        aadhar_id = request.POST['aadhar_id']
        phone = request.POST['phone']
        address = request.POST['address']

        try:
            aut.create_user_with_email_and_password(email, password)
            user_ids = fire_db.collection('User').list_documents()
            for x in user_ids:
                my_id = int(x.id)
            user_data = {
                'name': name,
                'email': email,
                'aadhar_id': aadhar_id,
                'phone': phone,
                'address': address,
                'cases': []
            }
            fire_db.collection('User').document(str(my_id + 1)).set(user_data)
            return redirect('login')
        except Exception as e:
            messages.info(request, "Either this Email-ID is taken or the password is less than 6 characters.")
            print('Exception: ', e)
            return redirect('user_register')

    else:
        try:
            if request.session['uid']:
                print('Session is active')
                return redirect('dashboard')
            else:
                raise KeyError
        except KeyError as e:
            print('Session is not active. Exception: ', e)
            return render(request, 'user_register.html')


def dashboard(request):
    try:
        if request.session['uid']:
            return render(request, 'dashboard.html')
        else:
            raise KeyError
    except KeyError as e:
        print("Session not active: ", e)
        return redirect('login')


def lawyer_register(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        # Expertise
        get_expertise = {
            'Divorce': request.POST.get('divorce', 'off'),
            'Crime': request.POST.get('crime', 'off'),
            'Documentation': request.POST.get('documentation', 'off'),
            'Property': request.POST.get('property', 'off')
        }

        expertise = []
        for x in get_expertise.keys():
            if get_expertise[x] == 'on':
                expertise.append(x)

        experience = request.POST['experience']
        bar_id = request.POST['bar_id']

        try:
            aut.create_user_with_email_and_password(email, password)
            lawyer_ids = fire_db.collection('Lawyers').list_documents()
            for x in lawyer_ids:
                my_id = int(x.id)
            user_data = {
                'name': name,
                'email': email,
                'expertise': expertise,
                'experience': experience,
                'phone': phone,
                'address': address,
                'bar_id': bar_id,
                'rating': 0
            }
            fire_db.collection('Lawyers').document(str(my_id + 1)).set(user_data)
            return redirect('login')
        except Exception as e:
            messages.info(request, "Either this Email-ID is taken or the password is less than 6 characters.")
            print('Exception: ', e)
            return redirect('lawyer_register')

    else:
        try:
            if request.session['uid']:
                print('Session is active')
                return redirect('dashboard')
            else:
                raise KeyError
        except KeyError as e:
            print('Session is not active. Exception: ', e)
            return render(request, 'lawyer_register.html')

