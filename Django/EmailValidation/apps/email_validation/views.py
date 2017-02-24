from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')


def index(request):
    return render(request, 'email_validation/index.html')

def success(request):
    context = {
        'email': Email.objects.order_by('-created_at')
    }

    return render(request, 'email_validation/result.html', context)


def process(request):
    if request.method != POST:
        return redirect
    if not re.match(EMAIL_REGEX, request.POST['email'])
    messages.error(request, 'Email is not valid!')
    return redirect('/')
    else:
        email = Email.objects.create(email = request.POST['email'])
        messages.success(request, 'The email address you entered %s is a VALID email address!  Thank you!' %email.email)
        return redirect('/success')


def destroy(request, id):
    email = Email.objects.get( id = id )
    email.delete()
    messages.success(request, 'Email address %s was successfully deleted' %email.email)
    return redirect('/success')
