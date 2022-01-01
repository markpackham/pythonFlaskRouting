from flask import Flask
app = Flask(__name__)

# to run, python -m flask run

@app.route('/')
def home():
    return 'No Ninjas here'