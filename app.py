from flask import Flask, render_template
app = Flask(__name__)

# to run, python -m flask run

@app.route('/')
def home():
    return 'No Ninjas here'


@app.route('/ninjas')
def home():
    return render_template('index.html',)