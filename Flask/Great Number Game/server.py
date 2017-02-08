from flask import Flask, render_template, request, redirect, session, flash
import random

app = Flask(__name__)
app.secret_key = '\x0co\xc4\r\x19E_\xc8m\x0e\x95\xee\xd8\xfb-y=\xaa\xc1N\xb5\xee\x14\xe7'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randrange(1, 101)
        print session['number']
    if 'guess' in session:
        if session['guess'] < session['number']:
            flash('Too Low!', 'red')
        elif session['guess'] > session['number']:
            flash('Too High!', 'red')
        elif session['guess'] == session['number']:
            flash(session['guess'] + ' was the number!', 'green')

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    # print session['guess']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('guess')
    session.pop('number')

    return redirect('/')

app.run(debug=True)
