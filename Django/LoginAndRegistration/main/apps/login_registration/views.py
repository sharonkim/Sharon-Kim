from __future__ import absolute_import
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User, UserManager


# Function to display registration/login form
def index(request):
    return render(request, 'login_registration/index.html')


# Function to register new user
def register(request):
    # Set data as variables for readability
    fname = request.POST['fname']
    email = request.POST['email']
    # Passing data from Users model and storing information
    user = User.objects.register(request.POST)
    # user.save(request.POST)
    print user, '<<<---------this is what we got back'
    # Validation errors saved as messages
    if user[0] is False:
        for error in user[1]:
            messages.error(request, error)

    else:
        print user
        # Save user in session if successful validation
        request.session['id'] = user[1].id
        request.session['user'] = user[1].fname
        # Validation success saved as message
        messages.success(request, 'Successfully registered (or logged in)!')

        return redirect('/success')

    print user, '<<<------------ this is what we got back from the function'
    # Reload index in case of error messages
    return redirect('/')


# Function to validate user login credentials
def login(request):
    # Setting data to variables for readability
    # email = request.POST['email']
    # password = request.POST['password']
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    # error = User.objects.login(request.POST)
    # Save user to session upon successful validation
    if user is not None:
        print user
        login(request, user)
        return redirect('/success')

    # If authentication fails, return error message
    else:
        return 'Email or password is incorrect'
    # Reload index to render messages
    return redirect('/')


# Function to render page upon successful registration/login
def success(request):
    return render(request, 'login_registration/success.html')


# Function to remove user from session
def logout(request):
    # if 'user' in request.session:
    #     request.session.pop('user')
    logout(request)

    # Reload index
    return redirect('/')
