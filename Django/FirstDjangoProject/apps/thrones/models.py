from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


class UserManager(models.Manager):
    def create_new_user(self, data):
        errors = []

        print 'I\'m getting passed this, ', data

        if len(data['first_name']) < 2:
            errors.append['First name must be at least two character']
        #
        # if not re.match(data['email'], EMAIL_REGEX):
        #     errors.append['Email must be valid']

        if errors:
            return (false, errors)
        else:
            new_user = User.objects.create(first_name=form_data['first_name'])
            return (True, new_user)


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.first_name
