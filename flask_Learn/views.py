from flask_Learn import app
from flask import render_template, flash, redirect
from .forms import LoginForm
@app.route('/index')
def index():
    return 'index Hello World!' \
           '' \
           '<div>Microblog: <a href="/hello">Home</a></div>'


@app.route('/')
@app.route('/hello')
def hello():
    user = {'nickname': 'Miguel'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {'author': {'nickname': 'Susan'},
         'body': 'The Avengers movie was so cool!'
         }
        ]
    # fake user
    return render_template('index.html', title='Home',
                           user=user, posts=posts)


# index view function suppressed for brevity

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/hello')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers=app.config['OPENID_PROVIDERS'])