from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from datetime import datetime


class Brandr(models.Manager):  # Registration form for new user registration
    brand_name = models.TextField(max_length = 50)

    def __str__(self):
        return self.brand_name

        class Meta:
            db_table = 'brands'


class Product(models.Model):
    bramd = models.ForeignKey(Brand)
    name = models.TextField(max_length = 75)
    price = models.FloatField(default = 1.00)
    date_added = models.DateTimeField(auto_now_add = True)
    descritpion = models.TextField(max_length = 200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
