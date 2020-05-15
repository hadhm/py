from sqlalchemy import create_engine, ForeignKey, Table, Column, String, Integer, Text, func
from sqlalchemy.orm import relationship
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from py import app
from app.models.base_model import db

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


class MUser(db.Model):
  __tablename__ = 'muser'
  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String(50), nullable=False)

  articles = relationship(
      'MArticle', cascade='save-update,delete', lazy='dynamic')

  def __repr__(self):
    return f'{self.username}'


# 1 to n
class MArticle(db.Model):
  __tablename__ = 'marticle'

  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String(50), nullable=False)
  content = Column(Text)

  user_id = Column(
      Integer,
      ForeignKey('muser.id', ondelete='cascade'),
      nullable=False,
  )
  user = relationship('MUser')

  def __repr__(self):
    return f'{self.title} - {self.content}'


def db_init():
  print('init')
  with app.app_context():
    db.drop_all()
    db.create_all()
  #
  u1 = MUser(username='dhm')
  u2 = MUser(username='dhm2')
  for i in range(1):
    a = MArticle(title=f'a{i+1}', content=f'content{i+1}')
    u1.articles.append(a)

  for i in range(1, 3):
    a = MArticle(title=f'a{i+1}', content=f'content{i+1}')
    u2.articles.append(a)
  with app.app_context():
    db.session.add_all([u1, u2])
    db.session.commit()


if __name__ == '__main__':
  # db_init()

  # with app.app_context():
  #   result = db.session.query(MUser.username, func.count(MArticle.id)).join(
  #       MArticle, MUser.id == MArticle.user_id).group_by(MUser.id).order_by(
  #           func.count(MArticle.id).desc())
  # print(result.all())

  manager.run()
