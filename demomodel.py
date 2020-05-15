from sqlalchemy import create_engine, ForeignKey, Table, Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from app.config import settings as config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class DemoUser(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String(50), nullable=False)

  extend = relationship(
      'DemoUserExtend', uselist=False, cascade='save-update,delete')
  articles = relationship(
      'DemoArticle', cascade='save-update,delete', lazy='dynamic')

  def __repr__(self):
    return f'{self.username}'


# 1 to 1
class DemoUserExtend(Base):
  __tablename__ = 'user_extend'
  id = Column(Integer, primary_key=True, autoincrement=True)
  scholl = Column(String(50))

  user_id = Column(
      Integer,
      ForeignKey('user.id', ondelete='cascade'),
      nullable=False,
  )
  # user = relationship('DemoUser', backref=backref('extend', uselist=False))
  user = relationship('DemoUser')

  def __repr__(self):
    return f'{self.scholl}'


# 1 to n
class DemoArticle(Base):
  __tablename__ = 'article'
  # __mapper_args__ = {
  #     'order_by': id.desc(),
  # }

  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String(50), nullable=False)
  content = Column(Text)

  user_id = Column(
      Integer,
      ForeignKey('user.id', ondelete='restrict'),
      nullable=False,
  )
  user = relationship('DemoUser')

  tags = relationship(
      'DemoTag',
      secondary='article_tag',
      cascade='save-update,delete',
  )

  def __repr__(self):
    return f'{self.title} - {self.content}'


# n to n
class DemoTag(Base):
  __tablename__ = 'tag'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)

  articles = relationship(
      'DemoArticle',
      secondary='article_tag',
      cascade='save-update,delete',
  )

  def __repr__(self):
    return f'{self.name}'


article_tag = Table(
    'article_tag',
    Base.metadata,
    Column(
        'article_id',
        Integer,
        ForeignKey('article.id', ondelete='cascade'),
        primary_key=True),
    Column(
        'tag_id',
        Integer,
        ForeignKey('tag.id', ondelete='cascade'),
        primary_key=True),
)


def db_init():
  Base.metadata.drop_all()
  Base.metadata.create_all()
  #
  u = DemoUser(username='dhm')
  ue = DemoUserExtend(scholl='spxy')
  u.extend = ue
  a1 = DemoArticle(title='a1', content='content')
  a2 = DemoArticle(title='a2', content='content')
  u.articles.append(a1)
  u.articles.append(a2)
  session.add(u)
  session.commit()


def deleteN(init=False):
  if init:
    db_init()
  u = session.query(DemoUser).first()
  session.delete(u.extend)
  session.commit()


def delete1(init=False):
  if init:
    db_init()
  # 在extend,articles上加nullable=False，使之不能删除
  u = session.query(DemoUser).first()
  session.delete(u)
  session.commit()


def addTag(init=False):
  if init:
    db_init()
  a = session.query(DemoArticle).first()
  tag = DemoTag(name='111')
  # a.tags.append(tag)
  tag.articles.append(a)
  session.add(tag)
  session.commit()


def deleteTag(init=False):
  if init:
    db_init()
  a = session.query(DemoArticle).first()
  # for tag in a.tags:
  #   session.delete(tag)
  a.tags = []
  session.commit()


if __name__ == '__main__':
  addTag(True)
  # deleteTag(False)

  # from sqlalchemy.orm.dynamic import AppenderQuery
  # u = session.query(DemoUser).get(1)
  # print(u.articles.filter(DemoArticle.id == 2).all())

  # articles = session.query(DemoArticle).order_by(DemoArticle.id.desc())[0:10]
  # print(articles)
