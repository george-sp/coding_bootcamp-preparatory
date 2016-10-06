from flask import Flask, url_for, flash, send_from_directory, request, redirect, render_template, session
from forms import ContactForm

app = Flask(__name__)

app.secret_key = 'random string'

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if (request.method == 'POST'):
        if (not request.form['name'] or not request.form['surname'] \
                or not request.form['email'] or not request.form['password']):
            flash('Please fill all the fields.', 'error')
        else:
            # to set a session variable use the statement
            session['name'] = request.form['name']
            return login()
    return render_template('new.html')
