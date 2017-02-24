from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


# Create your views here.
def index(request):
    context = {
        'username': 'SharonK',
        'first_name': 'SharonK',
        'a_list': User.objects.all(),
        'a_dict': {
            'username': 'SharonK',
            'first_name': 'SharonK',
            'a_list': [1,2,6,89,24]
        }
    }

    try:
        print request.session['jiujitsu']
    except KeyError:
        request.session['jiujitsu'] = 9

    print request.session.get('nunchuk'),
    print context['a_list'][0],
    print context['username'], '<<<----- our username',
    return render(request, 'thrones/index.html', context)

def process(request):
    if request.method = 'POST':
        print request.POST, '<<<----- here is post data'
        request.session['first_name'] = request.POST['first_name']

        returned_tuple = User.objects.create_new_user(request.POST)

        print returned_tuple, 'this is (boolean, error list or user object)'
        if returned_tuple[0] == True:
            request.session['name'] = returned_tuple[1].first_name
            return redirect('/')
        else:
            for err in returned_tuple[1]:
                messages.error(request, err)

        return redirect('/')

def success(request):
    pass
