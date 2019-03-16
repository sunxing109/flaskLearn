from flask import render_template, flash, redirect, url_for, Response

from .forms import LoginForm
from flask_babel import lazy_gettext
import flask
import cv2

blueprint = flask.Blueprint(__name__, __name__)


@blueprint.route('/index')
def index():
    return 'index Hello World!' \
           '' \
           '<div>Microblog: <a href="/hello">Home</a></div>'


@blueprint.route('/index2')
def fun_urlfor():
    return url_for('/index')


# @app.route('/')
@blueprint.route('/hello2')
@blueprint.route('/hello')
def hello():
    user = {'nickname': 'Miguel'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': lazy_gettext('Beautiful day in Portland!')
        },
        {'author': {'nickname': 'Susan'},
         'body': lazy_gettext('The Avengers movie was so cool!')
         }
    ]
    # fake user
    return render_template('index.html', title='Home',
                           user=user, posts=posts)


# index view function suppressed for brevity


@blueprint.route('/')
@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/hello')
    return render_template('login.html',
                           title=lazy_gettext(u'Sign In 22'),
                           form=form)


def get_frame(cap):
    frame = cap.read()[1]
    jpeg = cv2.imencode('.jpeg', frame)[1]
    print(jpeg)
    return jpeg.tobytes()

#
# @blueprint.route('/deal_video', methods=['GET', 'POST'])
# def deal_video():
#     cap = cv2.VideoCapture()
#
#     while 1:
#         ret, frame = cap.read()
#         # cv2.imshow("capture", frame)  # 显示
#         # if cv2.waitKey(100) & 0xff == ord('q'):  # 按q退出
#         #     break
#         # cv2.imwrite("example.png", frame)  # 将拍摄内容保存为png图片
#     # cap.release()  # 关闭调用的摄像头
#     # return Response(gen(Camera()),
#     #                 mimetype='multipart/x-mixed-replace; boundary=frame')
#     return Response(get_frame(cap),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    while True:
        ret, frame = camera.read()
        jpeg = cv2.imencode('.jpeg', open('./example.png'))[1]
        yield (b'--framern'
               b'Content-Type: image/jpegrnrn' + jpeg.tobytes + b'rn')
    return

@blueprint.route('/deal_video')
def deal_video():
    cap = cv2.VideoCapture('C:/Users/sunxingba/Desktop/picture/feidaou.mp4')

    return Response(gen(cap),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
