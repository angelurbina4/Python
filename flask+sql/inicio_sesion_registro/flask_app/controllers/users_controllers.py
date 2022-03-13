from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.users import User
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/register",methods=['POST'])
def register():
    print(request.form)
    
    if not request.form['legalAge']:
        flash('You must be of legal age')
        redirect('/')
    
    if not User.validate_info(request.form):
        return redirect('/')
    
    pwd = bcrypt.generate_password_hash(request.form['password'])
    
    print(pwd)
    
    form = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pwd
    }
    
    ses = User.create(form)
    print(ses)
    
    session['user_id'] = ses
    
    return redirect('/dashboard')

@app.route('/dashboard')
def show():
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        "id" : session['user_id']
    }
    
    user = User.get_by_id(data)
    
    return render_template("show.html", user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    print(request.form)
    
    if len(request.form['email']) < 1:
        flash("Enter an email", 'login')
        return redirect('/')
    
    user = User.get_by_email(request.form)
    
    if not user:
        flash("Unregistered email", 'login')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Incorrect password", 'login')
        return redirect('/')
    
    session['user_id'] = user.id

    return redirect('/dashboard')