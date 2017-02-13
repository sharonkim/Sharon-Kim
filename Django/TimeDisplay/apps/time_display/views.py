from django.shortcuts import render
from datetime import datetime

def index(request):

    date_time = datetime.now()
    context = {
        'date': date_time.strftime('%B %d, %Y'),
        'time': date_time.strftime('%I:%M%p')
    }
    print '******', context, '******'
    return render(request, 'index.html', context )
