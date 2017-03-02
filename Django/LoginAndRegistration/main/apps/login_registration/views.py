from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager


def index(request): # Function to display registration/login form
    return render(request, 'login_registration/index.html')


def register(request):  # Function to register new user
    fname = request.POST['fname']   # Set data as variables for readability
    email = request.POST['email']
    user = User.objects.register(request.POST)  # Passing data from User model
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
    password = request.POST['password']
    result = User.objects.login(email, password)    # Validate user information

    if result[0]:   # If user validation is successful, confirm success
        request.session['login'] = result[1].id
        messages.success(request, 'Successfully logged in!')
        return redirect('/success')

    else:   # If user validation fails, flash error message
        errorMessages = result[1]
        return render(request, 'login_registration/index.html', errorMessages)


def success(request):   # Function to render page upon successful registration/login
    return render(request, 'login_registration/success.html')


def logout(request):    # Function to remove user from session
    messages.success(request, 'You have been successfully logged out')
    return redirect('/')    # Reload index
