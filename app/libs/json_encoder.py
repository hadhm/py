from datetime import date, datetime

from flask.json import JSONEncoder as _JSONEncoder


class JSONEncoder(_JSONEncoder):

  def default(self, o):
    # 对date,datetime作特殊处理
    # datetime是date子类，判断要在前
    if isinstance(o, datetime):
      data = o.isoformat(sep=' ', timespec='seconds')
      # data = o.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(o, date):
      data = o.isoformat()
    elif hasattr(o, 'keys') and hasattr(o, '__getitem__'):
      data = dict(o)
    else:
      data = super().default(o)

    return data
