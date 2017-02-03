# Import Flask and all needed functions
from flask import Flask, render_template, request, redirect, session, flash
import re, datetime

# Define regular expressions
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'.*([a-zA-Z]).*')
PWD_REGEX = re.compile(r'((\w*[A-Z]{1,}\w*[0-9]{1,}\w*)|(\w*[0-9]{1,}\w*[A-Z]{1,}\w*))')
DOB_REGEX = re.compile(r'([0][1-9]|[1][0-2])\/([0][1-9]|[1-2][0-9]|[3][0-1])\/[0-9]{4}')

# Create flask object to set up the server and security key for the sessions
app = Flask(__name__)
app.secret_key = 'secret key'

# Load forms
@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')

# Validate submitted information
@app.route('/process', methods=['POST'])
def process():

# Email format validation
    if len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email address", "error")

# Name format validation
    if len(request.form['first_name']) < 1 or not NAME_REGEX.match(request.form['first_name']):
        flash("Please enter a valid FIRST name using only alphanumeric characters", "error")

    if len(request.form['last_name']) < 1 or not NAME_REGEX.match(request.form['last_name']):
        flash("Please enter a valid LAST name using only alphanumeric characters", "error")

# Password validation
    if len(request.form['password']) < 9 or not PWD_REGEX.match(request.form['password']):
        flash("Password must be at least 9 characters and contain 1 UPPERCASE letter and 1 number", "error")

    if request.form['confirm'] != request.form['password']:
        flash("Passwords DO NOT match", "error")
        print 'Password match'

# Birthdate validation
    minyear = 1900
    maxyear = datetime.date.today().year
    bday = request.form['dob'].split('/')

    if bday <= maxyear or bday > minyear or not DOB_REGEX.match(request.form['dob']):
        flash("Please enter a valid birthdate", "error")

# If valid information submitted
    else:
        flash("Thank you for sending your information, {}".format('first'), "correct")

    return redirect('/')

app.run(debug=True)
