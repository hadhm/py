from app import create_app
from app.models.base_model import db
from app.models.user import User

app = create_app()

with app.app_context():
  with db.auto_commit():
    su = User()
    su.email = '999@qq.com'
    su.password = '123456'
    su.nickname = 'Super'
    su.auth = 2
    db.session.add(su)
