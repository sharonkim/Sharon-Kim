from flask import Flask, render_template, request, redirect
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():

    name = request.form['name']
    dojo = request.form['dojo']
    language = request.form['language']
    comments = request.form['comments']

    return render_template('results.html', name=name, dojo=dojo, language=language, comments=comments)

@app.route('/process', methods=['POST'])
def process():
    success = True
    if len(request.form['name']) < 2:
        sucess = False
    if len(request.form['email']) not EMAIL_REGEX.match(request.form['email'])
        sucess = False
    if success:
        data = request.form
        return redirect('/process')
    else:
        retun redirect('/error')

@app.route('/process')
def process():
    return render_template('results.html')

@app.route('/error')
def wrong():
    return render_template('index.html')

app.run(debug=True)
