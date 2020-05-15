from sqlalchemy import inspect

from sqlalchemy import orm


class T():

  @orm.reconstructor
  def init_on_load(self):
    self._fields = []
    self.__exclude = []
    self._set_fields()
    self.__prune_fields()

  def _set_fields(self):
    pass

  def __prune_fields(self):
    inj = inspect(self).mapper.column_attrs
    print(inj)
    if not self._fields:
      all_columns = set(columns)
      self._fields = list(all_columns - set(self.__exclude))

  def hide(self, *args):
    for key in args:
      self._fields.remove(key)
    return self

  def keys(self):
    return self._fields

  def __getitem__(self, key):
    return getattr(self, key)


class my(T):
  x = 2
  y = 3

  def __init__(self, z):
    self.z = z


if __name__ == '__main__':
  t = my(4)
  t.init_on_load()
  print(dict(t))
