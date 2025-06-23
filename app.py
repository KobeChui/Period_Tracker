from flask import Flask, render_template, request, session, url_for, redirect, flash
from datetime import datetime, timedelta
from period_tracker import calculate_next_period, get_username
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy import text # textual queries

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes = 30)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class Person(db.Model):
    __tablename__ = 'Person'
    id = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    username = db.Column(db.String(20), unique=True, nullable = False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(130), nullable = False)
    acc_type = db.Column(db.String(10), nullable = False)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', pagename = "Home")

@app.route('/login', methods = ['GET', 'POST'])
def tracker():
    if request.method == 'GET':
        if 'name' in session:
            return redirect(url_for('home'))
        return render_template('login.html')
    
    username = request.form['Username']
    password = request.form['Password']
    person = Person.query.filter_by(username = username).first()

    if not person or password != person.password:
        flash('Please check your login details and try again', 'error')
        return render_template('login.html')

    session['username'] = username
    session['password'] = password
    session['acc_type'] = person.acc_type
    session.permanent = True

    return render_template("user_tracker.html", uername=username)

if __name__ == "__main__":
    app.run(debug=True)