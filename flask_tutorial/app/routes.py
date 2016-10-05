from flask import Flask, request, render_template
from forms import ContactForm

app = Flask(__name__)

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if (request.method == 'POST'):
        pass
    return render_template('new.html')
