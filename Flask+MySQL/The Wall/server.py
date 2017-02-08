# Import all modules needed
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

# Server and secret key setup
app = Flask(__name__)
app.secret_key = '\xa9$\xf4\x7f\xaeQ\xec0\x0f\xbf\x17`\xc5+\xfa0\x04\\A\x1a\xeb\x13\xd1\xf8'

# Create encryption object hashing operations
bcrypt = Bcrypt(app)

# Create MySQL connection object for DB operations
mysql = MySQLConnector(app,'wall')

# Create regular expression objects to validate name and email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


# # Landing page
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# # Registration validations and db operations
# @app.route('/register', methods=['POST'])
# def create():
#
#     # Validate first name format
#     if len(request.form['first_name']) < 2:
#         flash('First name must contain at least 2 characters and cannot include numbers')
#
#     # Validate last name format
#     if len(request.form['last_name']) < 2:
#         flash('Last name must contain at least 2 characters and cannot include numbers')
#
#     # Validate email format
#     if len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']):
#         flash('Please enter a valid email')
#
#     # Validate password not less than 8 characters
#     if len(request.form['password']) < 8:
#         flash('Password must contain at least 8 characters')
#
#     # Validate password match
#     if len(request.form['password']) != request.form['confirm']:
#             flash('Passwords do not match. Please re-enter')
#
#      # If valid registration and non-existing user account, redirect login
#      # Retrieve emails
#     query = 'SELECT email FROM users'
#     emails = mysql.query_db(query)
#
#     # Verify email does not already exist in DB
#     for email in emails:
#         if email['email'] == request.form['email']:
#             flash('Email has already been registered')
#
#     # Upon successful registration
#     # Encrypt password
#     pw_hash = bcrypt.generate_password_hash(request.form['password'])
#     # Set query to add new user
#     query = 'INSERT INTO `wall`.`users` (`first_name`, `last_name`, `email`, `password`, `created_at`,`updated_at`)\
#             VALUES (:first_name, :last_name, :email, :password, NOW(), NOW());'
#
#     # Create data dictionary
#     data = {
#         'first_name': request.form['first_name'],
#         'last_name':  request.form['last_name'],
#         'email': request.form['email'],
#         'password': pw_hash
#     }
#
#     # Execute query
#     mysql.query_db(query, data)
#
#     query = 'SELECT id\
#             FROM users\
#             WHERE email = :email'
#     data.pop('first_name')
#     data.pop('last_name')
#     data.pop('password')
#     user = mysql.query_db(query, data)
#     session['user'] = user[0]['id']
#
#     return redirect ('/wall')
#
#     # Redirect to main page
#     return redirect('/')


# Process authentication
@app.route('/login', methods=['POST'])
def login_route():
    # Retrieve user record
    query = 'SELECT id, password\
            FROM users\
            WHERE email = :email'
    data = {
        'email': request.form['email']
    }
    user = mysql.query_db(query, data)
    print users
    return redirect('/')

#     # Check for match
#     if data != data:
#         # No user match
#         flash('Incorrect username or password')
#         return redirect ('/')
#     # Successful match
#     elif bcrypt.check_password_hash(user[0]['password'], request.form['password']):
#         # Save user id in session
#         session['user'] = user[0]['id']
#         # Redirect to wall
#         return render_template('wall.html')
#     else:
#         # No match redirects user to main page
#         flash('Incorrect username or password')
#         return redirect ('/')
#
# # Load wall with messages and comments
# @app.route('/wall')
# def user_home():
#     # Query user information for personalized UI
#     query = 'SELECT first_name FROM users WHERE id = :id'
#     data = {
#         'id': session['user']
#         }
#     user = mysql.query_db(query, data)
#
#     # Query for messages
#     query = 'SELECT users.id AS user_id_pk, users.first_name, users.last_name, messages.id\
#             AS message_id_pk, messages.message, messages.created_at\
#             FROM users\
#             JOIN messages ON users.id = messages.user_id\
#             ORDER BY messages.created_at DESC'
#     messages = mysql.query_db(query)
#     # Query for comments
#     for message in messages:
#         query = 'SELECT users.first_name, users.last_name, comments.comment, comments.created_at\
#                 FROM users\
#                 JOIN comments ON users.id = comments.user_id\
#                 WHERE message_id = :message_id'
#         data = {
#             'message_id': message['message_id_pk']
#         }
#         # Create key-value pair that contains all nessage comments
#         message['comments'] = mysql.query_db(query, data)
#
#     # Render template and pass information
#     return render_template('wall.html', f_name=user[0]['first_name'], messages=messages, user=session['user'])
#
# # End session and redirect to main page upon user logout
# @app.route('/logout', methods=['POST'])
# def user_logout():
#     session['user'] = []
#     return redirect('/')
#
# # Adding new message
# @app.route('/new_message', methods=['POST'])
# def new_message():
#     # Set message data
#     query = 'INSERT INTO `wall`.`messages` (`message`, `created_at`, `updated_at`, `user_id`)\
#             VALUES (:message, NOW(), NOW(), :user_id);'
#     data = {
#         'user_id': session['user'],
#         'message':request.form['message']
#     }
#     user = mysql.query_db(query, data)
#     # Reload page after comment submission
#     return redirect('/wall')
#
# # Create and link comments to appropriate message
# @app.route('/comment', methods=['POST'])
# def comment():
#     # Add comment
#     query = 'INSERT INTO `wall`.`comments` (`message_id`,`user_id`,`comment`,`created_at`,`updated_at`)\
#             VALUES (:message_id,:user_id,:comment,NOW(),NOW());'
#     data = {
#         'message_id': request.form['message_identifier'],
#         'user_id': session['user'],
#         'comment':request.form['comment']
#     }
#     mysql.query_db(query, data)
#     # Reload page after comment submission
#     return redirect('/wall')
#
# # Set parameters for deleting messages
# @app.route('/delete', methods=['POST'])
# def destroy():
#     query = 'DELETE FROM messages\
#             WHERE id = :message_id'
#     data = {
#         'message_id': request.form['message_id']
#     }
#     mysql.query_db(query, data)
#     # Reload page after deleting message
#     return redirect ('/wall')
#
# app.run(debug=True)
