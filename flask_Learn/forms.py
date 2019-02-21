from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from utils import formstwo
# from flask_wtf.i18n import Translations
from flask_babel import lazy_gettext as _


class LoginForm(Form):

    # tran =Translations()
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

    dataset = formstwo.SelectField(
        _('Select Dataset'),
        choices=[],
        tooltip=_("Choose the dataset to use for this model.")
    )