from app.app import Flask
from flask_cors import CORS
from flask_mail import Mail

from app.models.base_model import db
from app.utils.alidayu import AlidayuAPI

mail = Mail()
alidayi = AlidayuAPI()


def register_blueprint(app):
  from app.api.v1 import create_blueprint_v1
  app.register_blueprint(create_blueprint_v1())


def register_plugin(app):
  db.init_app(app)
  with app.app_context():
    db.create_all()
  mail.init_app(app)
  # alidayi.init_app(app)


# 跨域支持
def after_request(resp):
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp


def create_app():
  app = Flask(__name__)

  # CORS(app)
  app.after_request(after_request)

  app.config.from_object('app.config.settings')
  app.config.from_object('app.config.secure')

  register_blueprint(app)
  register_plugin(app)

  return app
