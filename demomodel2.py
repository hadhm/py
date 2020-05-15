from sqlalchemy import create_engine, ForeignKey, Table, Column, String, Integer, Enum, Text, func
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
  gender = Column(Enum('secret', 'male', 'female'), default='secret')

  def __repr__(self):
    return f'{self.username}'


def db_init():
  u1 = User(username='张三', age=18, gender='male')
  u2 = User(username='李四', age=19, gender='female')
  u3 = User(username='王二', age=18, gender='male')
  u4 = User(username='刘晶', age=18, gender='male')
  u5 = User(username='赵八', age=18, gender='male')
  u6 = User(username='吴法', age=19, gender='male')
  u7 = User(username='张三', age=17, gender='male')
  u8 = User(username='小三', age=17, gender='male')
  u9 = User(username='大三', age=17, gender='female')
  u10 = User(username='赵三', age=18, gender='female')
  Base.metadata.drop_all()
  Base.metadata.create_all()
  session.add_all([u1, u2, u3, u4, u5, u6, u7, u8, u9, u10])
  session.commit()


if __name__ == '__main__':
  db_init()

  # result = session.query(User.age, func.count(User.id)).group_by(
  #     User.age).having(User.age >= 18).all()
  # print(result)

  # stmt = session.query(
  #     User.username.label('username'),
  #     User.age.label('age')).filter(User.username == '张三').subquery()
  # print(type(stmt))
  '''
  <class 'sqlalchemy.sql.selectable.Alias'>
  result = session.query(User).filter(User.username.like(f'{"张三"[:1]}%'))
  '''
  # result = session.query(User).filter(User.username == stmt.c.username,
  #                                     User.age == stmt.c.age)
  # print(result)
