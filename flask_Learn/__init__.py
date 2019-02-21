from flask import Flask
from flask_babel import Babel
app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans_CN'
#app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)
import config, flask_Learn.views, flask_Learn.forms
app.config.from_object(config)
app.register_blueprint(flask_Learn.views.blueprint)
app.register_blueprint(flask_Learn.views.blueprint)






