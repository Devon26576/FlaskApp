from flask import Flask

app = Flask(__name__)


@app.route('/')
def genius():
    return '<h1>hello, Genius!</h1>'

@app.route('/about/')
def about():
    return '<h3> It Feels Great to be a genius!</h3>' 
