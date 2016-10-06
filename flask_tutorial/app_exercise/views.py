from flask import Flask, render_template, request
from form import SignUpForm

app = Flask(__name__)

@app.route('/new', methods=['GET', 'POST'])
def new():
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug = True)
