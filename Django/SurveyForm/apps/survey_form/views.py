from django.shortcuts import render, redirect


def index(request):
        return render(request, 'survey_form/index.html')


def process(request):
    if request.method == 'POST':
        if 'attempt' in request.session:
            request.session['attempt'] += 1
        else:
            request.session['attempt'] = 1

        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

        return redirect('/result')
    else:
        return redirect('/')


def result(request):
    return render(request, 'survey_form/result.html')
