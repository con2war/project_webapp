from re import M
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from Website.models import User

recommendor = Blueprint('recommendor', __name__)

df = pd.read_csv(r"C:\Users\conor\Documents\Uni yr4\Project\WebApp\Website\datasets\meta_data.csv")

def get_suggestions():
    return list(df['model'].str.capitalize())

def create_similarity():
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['combined_features'])
    # creating a similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return df,similarity

def rcmd(m):
    m = m.lower()
    try:
        df.head()
        similarity.shape
    except:
        df, similarity = create_similarity()
    if m not in df['model'].unique():
        return ('Oops! The phone you searched is not in our database. Please check the spelling and try again, hint click the logo!')
    else:
        i = df.loc[df['model']==m].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:4]
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(df['model'][a])
        return l

@recommendor.route('/recommendor', methods=['GET'])
@login_required
def recommend():
    suggestions = get_suggestions()
    return render_template('recommend.html',suggestions=suggestions, user=current_user)

@recommendor.route('/recommendor', methods=["GET","POST"])
@login_required
def recommendation():
    suggestions = get_suggestions()
    phone = request.form['Phone']
    rc = rcmd(phone)
    if type(rc)==type('string'):
        return render_template('recommendation.html',user=current_user, suggestions=suggestions, prediction_text=(rc))
    else:
        m_str=",".join(rc)
        return render_template('recommendation.html',user=current_user,suggestions=suggestions, prediction_text=(m_str))

