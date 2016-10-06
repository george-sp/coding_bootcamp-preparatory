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

@app.route('/login', methods=['POST'])
def login():
    if 'name' in session:
        name = session['name']
        return 'You are logged in as ' + name + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

@app.route('/logout')
def logout():
   # remove the name from the session if it is there
   session.pop('name', None)
   return redirect(url_for('index'))
