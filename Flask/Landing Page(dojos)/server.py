from flask import Flask, render_template, request, redirect, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = '\x0co\xc4\r\x19E_\xc8m\x0e\x95\xee\xd8\xfb-y=\xaa\xc1N\xb5\xee\x14\xe7'

@app.route('/dojos/new', methods=['GET'])
def index():
    return render_template('dojos.html')

@app.route('/success', methods=['POST'])
def submit():
    success = True
    if len(request.form['alias']) < 2:
        success = False
    if len(request.form['country']) < 2:
        success = False
    if len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']):
        success = False
    if success:
        data = request.form
        return redirect('/process')
    else:
        return redirect('/error')

@app.route('/process')
def process():
    return render_template('success.html')

@app.route('/error')
def wrong():
    return render_template('error.html')

app.run(debug=True)
