from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from datetime import datetime
import bcrypt, re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._]+\.[a-zA-Z]*$')    # Regular expressions defined and set as variables for readability
NAME_REGEX = re.compile(r'.*([a-zA-Z]).*')  # Regular expressions defined and set as variables for readability


class UserManager(models.Manager):  # Registration form for new user registration
    def register(self, data):
        print data
        fname = data['fname']   # Data set as variables for readability
        lname = data['lname']
        email = data['email']
        today = datetime.today()
        password = data['password']
        c_password = data['c-password']
        errors = []

        if len(fname) < 1 or not NAME_REGEX.match(fname):   # First/Last name format validation
            errors.append('Please enter a valid FIRST name using only alphanumeric characters')

        if len(lname) < 1 or not NAME_REGEX.match(lname):
            errors.append('Please enter a valid LAST name using only alphanumeric characters')

        if len(email) < 9 or not EMAIL_REGEX.match(email):  # Email format validation
            errors.append('Please enter a valid email address')

        if User.objects.filter(email = email):  # Validate email has not been previously registered
            errors.append('Email address entered is already registered. Please login.')

        if len(password) < 8:   # Password format validation
            errors.append('Password must contain at least (8) characters')

        if c_password != password:  # Confirm password match
            errors.append('Passwords DO NOT match')


        minyear = 1900  # Set data as variables for readability
        maxyear = datetime.today().year
        birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d')
        print data['birthdate']

        if birthdate.year >= maxyear or birthdate.year < minyear:   # Validate birthdate entry
            print type(data['birthdate'])
            print len(data['birthdate'])
            errors.append('Please enter a valid birthdate')

        if errors:  # Return errors, upon failed validation
            return (False, errors)

        else:   # If registration succeeds, hash password and render success message
            password = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt()),
            user = self.create(fname=fname, lname=lname, email=email, password=password, birthdate=birthdate)
            return (True, user)


    def login(self, data):  # Login form for existing users
        user = User.objects.filter(email=data['email'])
        errors = []

        if not user or bycrypt.hashpw(data['password'].encode(), user.password.encode()) != user.password:  # If login info entered incorrectly, flash warning
            errors.append('Email or password is incorrect')
            print(False, errors)
            return(False, errors)

        if user:
            user = user[0]
            bycrypt.hashpw(data['password'].encode(), user.password.encode()) == user.password
            request.session['user_id'] = user.id
            request.session['email'] = user.email

            print(True, errors)
            return (True, user)


class User(models.Model):
    fname = models.CharField(max_length = 200)
    lname = models.CharField(max_length = 45)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    birthdate = models.DateField()
    objects = UserManager()

    def __str__(self):
        return self.fname
