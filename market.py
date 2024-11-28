from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return '<p> Hello World!</p>'

@app.route('/about/<username>')
def aboutPage(username):
    return f'<h1> This is a about page for {username}</h1>'
