from flask import render_template, redirect, url_for
from app import app
from app.forms import UserForm
import os

# Parallel dependencies
from app.indexScript import indexScript

title = 'Index Parallel'


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UserForm()
    return render_template('index.html', title=title, form=form)


@app.route('/benchmark', methods=['GET', 'POST'])
def benchmark():
    form = UserForm()
    if form.validate_on_submit():
        out = indexScript(form.term1.data, form.term2.data)
        return render_template("benchmark.html", title=title, result=out)
    return render_template("benchmark.html", title=title)

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
