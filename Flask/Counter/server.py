from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = '\x0co\xc4\r\x19E_\xc8m\x0e\x95\xee\xd8\xfb-y=\xaa\xc1N\xb5\xee\x14\xe7'

@app.route('/')
def counter():
    try:
        session['counter']
    except:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html')

@app.route('/add2', methods=['POSt'])
def increment():
    # print 'hi.'
    session['counter'] += 1
    return redirect('/')

@app.route('/reset_count', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
