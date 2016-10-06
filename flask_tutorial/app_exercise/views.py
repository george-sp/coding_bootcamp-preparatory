from flask import Flask, render_template, request, flash
from form import SignUpForm

app = Flask(__name__)

app.secret_key = 'random string'

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if the customer has filled all the fields
        if (not request.form['name'] or not request.form['surname'] \
                or not request.form['email'] or not request.form['password']):
            flash('All the fields are required to sign up.', 'error')
        # If there are errors, open the new.html
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug = True)
