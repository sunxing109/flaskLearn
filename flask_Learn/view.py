from flask_Learn import app
from flask import render_template

@app.route('/')
@app.route( '/index')
def index():
    return 'index Hello World!'

@app.route('/hello')
def hello():
    user = {'nickname': 'Miguel'}
    # fake user
    return render_template('index.html', title = 'Home',
        user = user)

# if __name__ == '__main__':
#     app.run()
