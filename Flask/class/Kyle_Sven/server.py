from flask import Flask, request, render_template, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a SECRET_KEY'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['GET','POST']) # was there a parameter
def submit():
    success = True
    if len(request.form['first']) < 2:
        flash('First name must be at least 2 characters', 'error')
        success = False
    if len(request.form['last']) < 2:
        flash('Last name must be at least 2 characters', 'error')
        success = False
    if len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']):#
        flash('Invalid Email', 'error')
        success = False

    if success:
        flash('Success', 'info')
        data = request.form
        return render_template('user.html', user=data)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
