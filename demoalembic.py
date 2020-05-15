from sqlalchemy import create_engine, ForeignKey, Table, Column, String, Integer, Text
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
  age = Column(Integer)

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
  u = User(username='dhm')
  a1 = Article(title='a1', content='content')
  a2 = Article(title='a2', content='content')
  u.articles.append(a1)
  u.articles.append(a2)
  session.add(u)
  session.commit()


if __name__ == '__main__':
  db_init()
