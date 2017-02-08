from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app, 'usersdb')
bcrypt = Bcrypt(app)
# Email reguar expression
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-z]*$')

# Password regular expression
password_regex = re.compile(r'(?=.{8,})')

# Main page
@app.route('/')
def index():
    return render_template('index.html')

# Register New User
@app.route('/users', methods=['POST'])
def create():
    # Set error test
    error = False

    # Validate first name format
    if len(request.form['first_name']) < 2:
        flash("First Name must be greater than 2 characters!")
        error = True
    # Validate last name format
    if len(request.form['last_name']) < 2:
        flash("Last Name must be greater than 2 characters!")
        error = True

    # Query DB for matching record
    email_query = 'SELECT * FROM users WHERE email = :email'
    email_data = {
                'email': request.form['email'],
    }
    validate_email = mysql.query_db(email_query, email_data)
    # Validate email address format
    if not email_regex.match(request.form['email']):
        flash("Invalid Email Address!")
        error = True
    # Validate email address is not already registered
    elif validate_email:
        flash("Email is already in use!")
        error = True
    # Validate password format
    if not password_regex.match(request.form['password']):
        flash("Password must contain at least 8 characters!")
        error = True
    # Validate passwords match
    elif not request.form['confirm_password'] == request.form['password']:
        flash("Password does not match!")
        error = True
    # Redirect user to the main page if information cannot be validated
    if error:
        return redirect('/')
    # User information stored in DB if information is validated
    # Redirect to login page
    else:
        # Encrypt password
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        query = 'INSERT INTO users (first_name, last_name, email, password, \
                created_at, updated_at) \
                VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'
        data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'password': pw_hash
        }
        mysql.query_db(query, data)
        # Session information to be diplayed on login page
        session['user'] = {
                'first_name': data['first_name'],
                'last_name': data['last_name'],
        }
        return render_template('success.html')

# User logged in if credentials are entered correctly
@app.route('/login', methods=['POST'])
def login():
    # Set error test for login validation
    error = False
    data = {
            'email': request.form['email'],
            'password': request.form['password']
    }
    query = 'SELECT * FROM users WHERE email = :email'
    user = mysql.query_db(query, data)
    # Validate login information
    if not user or not bcrypt.check_password_hash(user[0]['password'], data['password']):
        flash("Email or password are incorrect.  Please re-enter inforamtion.")
        error = True
    # Redirect to main page if login credentials cannot be validated
    if error:
        return redirect('/')
    else:
        # Information stored into DB and displayed for session
        session['user'] = {
                'id': user[0]['id'],
                'first_name': user[0]['first_name'],
                'last_name': user[0]['last_name'],
        }
        return render_template('success.html')

# Option to logout of current session
@app.route('/logout')
def logout():
    # Terminate current session and destroy user info
    del session['user']
    return redirect('/')

@app.route('/retrieve')
def retrieve():
    return render_template('update.html')

# User password update
@app.route('/update', methods=['POST'])
def update():
    # Set errpr test
    error = False
    user_query = 'SELECT * FROM users WHERE email = :email'
    user_data = {
            'email': request.form['email'],
            'password': request.form['new_password']
    }
    validate_user = mysql.query_db(user_query, user_data)
    # query for matching user record in DB
    if not validate_user:
        flash("Invalid email!")
        error = True
    # Confirms password has been changed
    if bcrypt.check_password_hash(validate_user[0]['password'], user_data['password']):
        flash("New password cannot be the same as old password!")
        error = True
    # Validates email address
    elif not password_regex.match(request.form['new_password']):
        flash("New password must contain at least 8 characters!")
        error = True
    elif not request.form['confirm_new_pw'] == request.form['new_password']:
        flash("New password does not match!")
        error = True
    # Redirect to main page if email and password cannot be validated
    if error:
        return render_template('update.html')
    # Records new encrypted password into DB and redirects to main page
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['new_password'])
        query = 'UPDATE users \
                SET password = :password, updated_at = NOW() \
                WHERE email = :email'
        data = {
                'email': request.form['email'],
                'password': pw_hash
        }
        mysql.query_db(query, data)
        return redirect('/')

app.run(debug=True)
