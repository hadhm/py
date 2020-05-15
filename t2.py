from flask import json


def __getitem__(self, item):
  return getattr(self, item)


def keys(self):
  return self.__keys


class Base():
  __keys = []


class User(Base):
  a = 1
  b = 2
  c = 3
  __keys = ['a', 'b', 'c']

  def __init__(self):
    print(type(self).__dict__)
    # type(self).__dict__['keys'] = keys
    # type(self).__dict__['__getitem__'] = __getitem__


User()

# print(json.dumps(dict(User())))