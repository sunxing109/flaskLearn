from flask import Flask
from flask_babel import Babel
app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans_CN'
babel = Babel(app)
import config
app.config.from_object(config)


from flask_Learn import views



