from flask import Blueprint, render_template, request, flash, redirect
from psutil import users
from Website.auth import admin
from .models import Admin, User
from . import db
from flask_login import login_required, current_user

updateuser = Blueprint('updateuser', __name__)

@updateuser.route('/dashboard', methods =['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html', user = current_user)

@updateuser.route('/admindashboard', methods =['GET','POST'])
def admindashboard():
    all_data = User.query.all()
    return render_template('admindashboard.html', users = all_data)

@updateuser.route('/update/<int:id>', methods =['GET','POST'])
def update(id):
    user_to_update = User.query.get_or_404(id)
    if request.method == "POST":
        user_to_update.email = request.form['email']
        try:
            db.session.commit()
            return redirect('/dashboard')
        except:
            return "There was a problem"
    else:
        return render_template('update.html', user_to_update=user_to_update, user=current_user)#

@updateuser.route('/delete/<int:id>', methods =['GET','POST'])
def delete(id):
    user_to_delete = User.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect('/sign-up')
    except:
        return "There was a problem"

@updateuser.route('/adminupdate', methods=['GET', 'POST'])
def adminupdate():
    if request.method == 'POST':
        my_data = User.query.get(request.form.get('id'))
 
        my_data.first_name = request.form['name']
        my_data.email = request.form['email']
 
        db.session.commit()
        flash("User Updated Successfully")
 
        return redirect('/admindashboard')
    
@updateuser.route('/admindelete/<int:id>', methods =['GET','POST'])
def admindelete(id):
    user_to_delete = User.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("User deleted successfully")
        return redirect('/admindashboard')
    except:
        flash("There was a problem, try again")
        return redirect('/admindashboard')