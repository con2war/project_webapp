from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import pandas as pd
import numpy as np

from Website.models import User

search = Blueprint('search', __name__)

df = pd.read_csv(r"C:\Users\conor\Documents\Uni yr4\Project\WebApp\Website\datasets\basic.csv")
df.to_html(render_links=True, escape=False)

def get_suggestions():
    return list(df['model'])

def phonesearch(m):
    i = df.loc[df['model']==m]
    for row in df:
        if i == row[1]:
            print (row)

def srch(m):
    if m not in df['model'].unique():
        return render_template('error.html', user=current_user)
    else:
        i = df.loc[df['model']==m]
        sorted_search = i
        return sorted_search

@search.route('/search', methods=['GET'])
@login_required
def searcher():
    suggestions = get_suggestions()
    return render_template('search.html',suggestions=suggestions, user=current_user)

@search.route('/search', methods=["GET","POST"])
@login_required
def result():
    suggestions = get_suggestions()
    phone = request.form['Phone']
    sh = srch(phone)
    print (sh)
    if type(sh)==type(''):
        return render_template('error.html',user=current_user,suggestions=suggestions)
    else:
        return render_template('search_result.html',user=current_user, suggestions=suggestions, search_text=(sh))


