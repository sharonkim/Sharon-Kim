from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        if len(request.form['name']) < 2:
            flash('Name must be at least two (2) characters')
            return redirect('/');
        if len(request.form['comment']) > 120:
            flash('Comments must not exceed 120 characters')
            return redirect('/');
    else:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return redirect('/results')

    return render_template('results.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

app.run(debug=True)
