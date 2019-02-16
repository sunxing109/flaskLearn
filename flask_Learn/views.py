from flask_Learn import app,babel
from flask import render_template, flash, redirect
from .forms import LoginForm
from flask.ext.babel import gettext


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
            'body': gettext('Beautiful day in Portland!')
        },
        {'author': {'nickname': 'Susan'},
         'body': gettext('The Avengers movie was so cool!')
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
        title = gettext('Sign In'),
        form = form,
        providers=app.config['OPENID_PROVIDERS'])

# @babel.localeselector
# def get_locale():
#     return 'zh_Hans_CN'