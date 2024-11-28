# Imports:
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#Instances:
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
# Model Class For Item:
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    def __repr__(self):
        return f'Item {self.name}'
# Home Routing:
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
# Login Routing:
@app.route('/login')
def login_page():
    return render_template('login.html')
# Signup Routing:
@app.route('/signup')
def signup_page():
    return render_template('signup.html')
# Market Routing:
@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
