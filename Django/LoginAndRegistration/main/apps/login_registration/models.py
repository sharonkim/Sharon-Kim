from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from datetime import datetime
import bcrypt, re

# Regular expressions defined and set as variables for readability
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'.*([a-zA-Z]).*')
# DOB_REGEX = re.compile(r'([0][1-9]|[1][0-2])\/([0][1-9]|[1-2][0-9]|[3][0-1])\/[0-9]{4}')


# Registration form for new user registration
class UserManager(models.Manager):
    def register(self, data):
        # print data
        # Data set as variables for readability
        fname = data['fname']
        lname = data['lname']
        email = data['email']
        today = datetime.today()
        password = data['password']
        c_password = data['c-password']
        errors = []

        # First/Last name format validation
        if len(fname) < 1 or not NAME_REGEX.match(fname):
            errors.append('Please enter a valid FIRST name using only alphanumeric characters')

        if len(lname) < 1 or not NAME_REGEX.match(lname):
            errors.append('Please enter a valid LAST name using only alphanumeric characters')

        # Email format validation
        if len(email) < 9 or not EMAIL_REGEX.match(email):
            errors.append('Please enter a valid email address')

        # Validate email has not been previously registered
        if User.objects.filter(email = email):
            errors.append('Email address entered is already registered. Please login.')

        # Password format validation
        if len(password) < 8:
            errors.append('Password must contain at least (8) characters')

        # Confirm password match
        if c_password != password:
            errors.append('Passwords DO NOT match')

        # Set data as variables for readability
        minyear = 1900
        maxyear = datetime.today().year
        birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d')
        print data['birthdate']

        # Validate birthdate entry
        if birthdate.year >= maxyear or birthdate.year < minyear:
            print type(data['birthdate'])
            print len(data['birthdate'])
            errors.append('Please enter a valid birthdate')

        # Return errors, upon failed validation
        if errors:
            return (False, errors)

        # If registration succeeds, hash password and render success message
        else:
            # print (False, errors)
            password = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt()),
            user = self.create(fname=fname, lname=lname, email=email, password=password, birthdate=birthdate)
            # print True
            return (True, user)


    # Login form for existing users
    def login(self, data):
        user = User.objects.filter(email=data['email'])
        errors = []
        # If login info entered incorrectly, flash warning
        if not user or bycrypt.hashpw(data['password'].encode(), user.password.encode()) != user.password:
            errors.append('Email or password is incorrect')

            # print(False, errors)
            return(False, errors)

        if user:
            user = user[0]
            bycrypt.hashpw(data['password'].encode(), user.password.encode()) == user.password
            request.session['user_id'] = user.id
            request.session['email'] = user.email

            # print(True, errors)
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
