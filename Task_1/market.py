from flask import Flask # Importing Flask Instance From Entire Flask Package
app = Flask(__name__) # Creating const App Like: Express.js

@app.route('/') # Get API ROUTING Decorator! One Step Before Function Root URL Of The Website!
def helloworld(): # Function To Be Envoked While Function Call!
    return '<h1>Hello World!</h1>' #Returns Value!

@app.route('/about/<username>')
def about_page(username):
    return f'<h1> Welcome User: {username}</h1>'