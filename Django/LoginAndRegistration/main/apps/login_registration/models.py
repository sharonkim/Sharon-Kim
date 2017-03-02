from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from datetime import datetime
import bcrypt, re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._]+\.[a-zA-Z]*$')    # Regular expressions defined and set as variables for readability
NAME_REGEX = re.compile(r'.*([a-zA-Z]).*')  # Regular expressions defined and set as variables for readability


class UserManager(models.Manager):  # Registration form for new user registration
    def register(self, data):
        fname = data['fname']   # Setting data as variables for readability
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
            errors.append('Confirmation password does not match')


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
            pw_bytes = password.encode('utf-8')
            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user = User.objects.create(fname=fname, lname=lname, email=email, password=password, birthdate=birthdate)
            return (True, user)


    def login(self, email, password):  # Login form for existing users
        errors = {}
        try:
            user = User.objects.get(email=email)

        except:
            user = 'None'

        if user == 'None':
            errors['noEmail'] = 'Email or password is incorrect'

        else:
            hash = user.password.encode('utf-8')
            pw_bytes = password.encode('utf-8')
            if bcrypt.hashpw(pw_bytes, hash) != hash:
                errors['noEmail'] = 'Email or password is incorrect'

        if len(errors) is not 0:
            return(False, errors)

        else:
            return(True, user)


class User(models.Model):
    fname = models.CharField(max_length = 200)
    lname = models.CharField(max_length = 45)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    birthdate = models.DateField()
    objects = UserManager()

    def __str__(self):
        return self.fname
