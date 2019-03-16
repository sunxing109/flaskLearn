from flask import Flask
from flask_babel import Babel
import flask_Learn.views, flask_Learn.forms
import settings
app = Flask(__name__, template_folder='flask_Learn/templates')
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans_CN'

babel = Babel(app)

app.config.from_object(settings)
app.register_blueprint(flask_Learn.views.blueprint)
app.register_blueprint(flask_Learn.views.blueprint)

app.run()
