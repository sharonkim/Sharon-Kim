from flask import Flask, request, session, render_template, redirect
from time import gmtime, strftime
import random

app = Flask(__name__)
app.secret_key = '\x0co\xc4\r\x19E_\xc8m\x0e\x95\xee\xd8\xfb-y=\xaa\xc1N\xb5\xee\x14\xe7'

@app.route('/')
def index():
    print 'A'*50
    if 'gold' not in session:
        session['gold'] = 0
        print '1'*50
        return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        gold = random.randrange(10, 21)
        activity = 'Earned {} golds from the farm!'.format(gold)
        process = 'earned'
    elif request.form['building'] == 'cave':
        gold = random.randrange(5, 11)
        activity = 'Earned {} golds from the cave!'.format(gold)
        process = 'earned'
    elif request.form['building'] == 'house':
        gold = random.randrange(2, 6)
        activity = 'Earned {} golds from the house!'.format(gold)
        process = 'earned'
    elif request.form['building'] == 'casino':
        gold = random.randrange(0, 51)
        gamble = random.randint(0, 2)
        if gold == 0:
            activity = 'Earned {} golds from the casino!'.format(gold)
            process = 'earned'
        else:
            activity = 'Lost {} golds from the casino...Ouch!'.format(gold)
            process = 'red'
    session['gold'] += gold
    date = strftime("(%Y/%m/%d %I:%M %p)", gmtime())
    activity = activity + " " + date
    if 'activities' not in session:
        session['activities'] = []
    else:
        session['activities'].append([activity, process])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['gold'] = 0
    session['activities'] = []
    return redirect('/')

app.run(debug=True)
