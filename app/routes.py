from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import UserForm
import os

# Parallel dependencies
from app.indexScript import indexScript


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        out = indexScript(form.term1.data, form.term2.data)
        return render_template('index.html', title='Index Parallel', result=out, form=form)
    return render_template('index.html', title='Index Parallel', form=form)

# def index():
#     out = indexScript("brother", "water")
#     print(out['t1'])
#
#     user = {'username': "Jack"}
#     posts = [
#         {
#             'author': {'username': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'username': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template('index.html', title='Home', user=user, posts=posts,benchmark_out=out)
