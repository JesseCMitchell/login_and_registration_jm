from flask_app import app, bcrypt
from flask import render_template, redirect, session, request

from flask_app.models import model_user

@app.route('/user/login', methods=['POST'])
def user_new():
    #validate user
    model_user.User.validate_login(request.form)
    return redirect('/')

@app.route('/user/logout')
def user_logout():
    del session['uuid']
    return redirect('/')

@app.route('/user/create', methods=['POST'])
def user_create():
    # validate user
    if not model_user.User.validate(request.form):
        return redirect('/')

    # hash the password
    hash_password = bcrypt.generate_password_hash(request.form['password'])

    data = {
        **request.form, 
        'password': hash_password
    }
    
    user_id = model_user.User.create(data)
    session['uuid'] = user_id
    return redirect('/') 

@app.route('/user/<int:id>')
def user_show(id):
    return render_template('user_show.html')