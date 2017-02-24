from django.shortcuts import render, redirect
import string, random


def index(request):
    return render(request, 'random_word_generator/index.html')

def process(request):
    if 'attempt' in request.session:
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1

    chars = ''.join(( string.uppercase, string.digits ))
    random_string = ''.join( random.choice( chars ) for i in range(14) )
    print (random_string, '*' * 20)
    request.session['random_string'] = random_string
    return redirect('/')
