from django.shortcuts import render, redirect
from time import gmtime, strftime
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'activities' not in request.session:
        request.session['activities'] = []

    context = {
        'activities': request.session['activities']
    }

    context['activities'].reverse()

    return render(request, 'ninja_gold/index.html', context)


def process_money(request, building):
    if request.method == 'POST':
        if building == 'farm':
            gold = random.randrange(10, 21)
            activity = 'Earned {} golds from the farm!'.format(gold)
            process = 'earned'

        elif  building == 'cave':
            gold = random.randrange(5, 11)
            activity = 'Earned {} golds from the cave!'.format(gold)
            process = 'earned'

        elif building == 'house':
            gold = random.randrange(2, 6)
            activity = 'Earned {} golds from the house!'.format(gold)
            process = 'earned'

        elif building == 'casino':
            gold = random.randrange(0, 51)
            gamble = random.randrange(0, 2)
            if gamble == 0:
                activity = 'Earned {} golds from the casino!'.format(gold)
                process = 'earned'

            else:
                activity = 'Entered a casino and lost {} golds... Ouch..'.format(gold)
                gold = gold * -1
                process = 'lost'

        request.session['gold'] += gold
        date = strftime( '(%Y/%m/%d %I:%m %p)', gmtime() )
        activity = activity + ' ' + date
        request.session['activities'].append( [activity, process] )
        return redirect('/')

    else:
        return redirect('/')


    def reset(request):
        request.session.delete()
        return redirect('/')
