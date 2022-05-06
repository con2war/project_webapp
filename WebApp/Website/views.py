from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)
    
@views.route('/', methods=["POST","GET"])
@login_required
def home():
    return render_template('home.html',  user = current_user)

@views.route('/adminhome', methods=["POST","GET"])
def adminhome():
    return render_template('adminhome.html',  user = current_user)
