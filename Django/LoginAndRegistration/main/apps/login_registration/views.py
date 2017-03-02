from __future__ import absolute_import
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User, UserManager


def index(request): # Function to display registration/login form
    return render(request, 'login_registration/index.html')


def register(request):  # Function to register new user
    fname = request.POST['fname']   # Set data as variables for readability
    email = request.POST['email']   # Set data as variables for readability
    user = User.objects.register(request.POST)  # Passing data from Users model and storing information
    print user, '<<<---------this is what we got back'

    if user[0] is False:    # Validation errors saved as messages
        for error in user[1]:
            messages.error(request, error)

    else:
        print user
        request.session['id'] = user[1].id  # Save user in session if successful validation
        request.session['user'] = user[1].fname
        messages.success(request, 'Successfully registered!')   # Validation success saved as message
        return redirect('/success')

    print user, '<<<------------ this is what we got back from the function'
    return redirect('/')    # Reload index in case of error messages


def login(request): # Function to validate user login credentials
    email = request.POST['email']   # Setting data to variables for readability
    password = request.POST['password'] # Setting data to variables for readability
    user = authenticate(email=email, password=password) # Setting data to variables for readability

    if user is not None:    # Save user to session upon successful validation
        print email
        login(request, user)
        messages.success(request, 'Successfully logged in!')
        return redirect('/success')

    else:   # If authentication fails, return error message
        messages.error(request, 'Email or password is incorrect')
        return redirect('/')


def success(request):   # Function to render page upon successful registration/login
    return render(request, 'login_registration/success.html')


def logout(request):    # Function to remove user from session
    return redirect('/')    # Reload index
