from django.shortcuts import render


def index(request):
    return render(request, 'disappearing_ninjas/index.html')


def ninjas(request):
    return render(request, 'disappearing_ninjas/ninjas.html')


def show(request, color):
    if color == 'blue':
        ninja = 'Leonardo'

    elif color == 'orange':
        ninja = 'Michaelangelo'

    elif color == 'red':
        ninja = 'Raphael'

    elif color == 'purple':
        ninja = 'Donatello'

    else:
        ninja = 'April'

    context = {
        'color': color,
        'ninja': ninja
    }

    return render(request, 'disappearing_ninjas/show.html', context)
