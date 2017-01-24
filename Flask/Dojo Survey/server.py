from flask import Flask, render_template, request, redirect

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

app.run(debug=True)
