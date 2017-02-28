from __future__ import absolute_import
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User, UserManager


# Function to display registration/login form
def index(request):
    # if 'user_id' not in request.session:
    #     request.session['user_id'] = 0
    return render(request, 'login_registration/index.html')


# Function to register new user
def register(request):
    # Set data as variables for readability
    fname = request.POST['fname']
    # lname = request.POST['lname']
    email = request.POST['email']
    # password = request.POST['password']
    # c_password = request.POST['c-password']
    # errors = User.objects.register(request.POST)
    # Passing data from Users model and storing information
    my_tuple = User.objects.register(request.POST)
    # user.save(request.POST)
    print my_tuple, '<<<---------this is what we got back'
    # Validation errors saved as messages
    if my_tuple[0] is False:
        for error in my_tuple[1]:
            messages.error(request, error)

    else:
        print my_tuple
        # Save user in session if successful validation
        request.session['id'] = my_tuple[1].id
        request.session['user'] = my_tuple[1].fname
        # Validation success saved as message
        messages.success(request, 'Successfully registered (or logged in)!')

        return redirect('/success')

    print my_tuple, '<<<------------ this is what we got back from the function'
    # Reload index in case of error messages
    # print '1'*50
    # print request, errors
    return redirect('/')


# Function to validate user login credentials
def login(request):
    # Setting data to variables for readability
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    # Save user to session upon successful validation
    if user is not None:
        return redirect('/success')

    # If authentication fails, return error message
    else:
        return 'Invalid login information'
    # Reload index to render messages
    return redirect('/')


# Function to render page upon successful registration/login
def success(request):
    return render(request, 'login_registration/success.html', user)


# Function to remove user from session
def logout(request):
    if user in request.session:
        request.session.pop(user)

    # Reload index
    return redirect('/')
