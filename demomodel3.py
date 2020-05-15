from sqlalchemy import create_engine, ForeignKey, Table, Column, String, Integer, Text, func
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from app.config import settings as config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String(50), nullable=False)

  articles = relationship(
      'Article', cascade='save-update,delete', lazy='dynamic')

  def __repr__(self):
    return f'{self.username}'


# 1 to n
class Article(Base):
  __tablename__ = 'article'

  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String(50), nullable=False)
  content = Column(Text)

  user_id = Column(
      Integer,
      ForeignKey('user.id', ondelete='cascade'),
      nullable=False,
  )
  user = relationship('User')

  def __repr__(self):
    return f'{self.title} - {self.content}'


def db_init():
  Base.metadata.drop_all()
  Base.metadata.create_all()
  #
  u1 = User(username='dhm')
  u2 = User(username='dhm2')
  for i in range(1):
    a = Article(title=f'a{i+1}', content=f'content{i+1}')
    u1.articles.append(a)

  for i in range(1, 3):
    a = Article(title=f'a{i+1}', content=f'content{i+1}')
    u2.articles.append(a)

  session.add_all([u1, u2])
  session.commit()


if __name__ == '__main__':
  db_init()

  # result = session.query(User.username, func.count(Article.id)).join(
  #     Article, User.id == Article.user_id).group_by(User.id).order_by(
  #         func.count(Article.id).desc())
  # print(result)
