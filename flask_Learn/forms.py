from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired
from flask_babel import lazy_gettext as _


class LoginForm(FlaskForm):

    # tran =Translations()
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

    dataset = SelectField(
        'Select Dataset',
        validators=[DataRequired()],
        choices=[('name', 'lable'), ('xiaoxi', '小溪')]
    )
