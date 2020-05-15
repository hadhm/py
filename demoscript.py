from flask_script import Manager

from py import app
from app.models.user import User
from app.models.base_model import db

manager = Manager(app)


@manager.command
def init():
  print('init')
  with app.app_context():
    db.drop_all()
    db.create_all()


@manager.option('-u', '--username', dest='username')
@manager.option('-a', '--age', dest='age')
def add_user(username, age):
  print(f'{username} - {age}')


@manager.option('-n', '--nickname', dest='nickname', required=True)
@manager.option('-e', '--email', dest='email', required=True)
@manager.option('-s', '--secret', dest='secret', required=True)
@manager.option('-a', '--auth', dest='auth')
def register_by_email(nickname, email, secret, auth=1):
  u = User()
  u.nickname = nickname
  u.email = email
  u.password = secret
  u.auth = auth
  with app.app_context():
    with db.auto_commit():
      db.session.add(u)


if __name__ == '__main__':
  manager.run()
