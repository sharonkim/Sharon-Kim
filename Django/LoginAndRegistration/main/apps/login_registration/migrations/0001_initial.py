# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('birthdate', models.DateField()),
            ],
        ),
    ]
