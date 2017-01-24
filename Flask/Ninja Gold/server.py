from flask import Flask, request, session, render_template, redirect
from time import gmtime, strftime
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'

@app.route('/')
def index():
    try:
        session['gold']
    except:
        session['gold'] = 0
        return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    try:
        session['history']
    except:
        session['history'] = []

        action = request.form['action']
        gold = 0
        statement = ["green", ""]
        time = strftime("(%Y-%m-%d %H:%M:%S)", gmtime())
        if action == 'farm':
            gold = randint(10,20)
            statement[1] = "Earned " + str(gold) + " from the farm!  " + time
        elif action == 'cave':
            gold = randint(5,10)
            statement[1] = "Earned " + str(gold) + " from the cave!  " + time
        elif action == 'house':
            gold = randint(2,5)
            statement[1] = "Earned " + str(gold) + " from the house!  " + time
        elif action == 'casino':
            gold = randint(-50,50)
            statement[1] = "Entered a casino and "
            if gold < 0:
                statement[1] += "lost " + str(gold)[1:] + " golds ... Ouch. " + time
                statement[0] = "red"
            else:
                statement[1] += "Earned " + str(gold) + "golds ... Nice! " + time

        if statement:
            session['history'] = [statement] + session['history']

        try:
            session['gold'] += gold
        except:
            session['gold'] = gold
        # print 'gold', session['gold']
        # print 'history', session['history']
        return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['gold'] = 0
    session['history'] = []
    return redirect('/')

app.run(debug=True)
