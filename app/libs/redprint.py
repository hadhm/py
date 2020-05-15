class Redprint():

  def __init__(self, name):
    self.name = name
    self.mound = []

  def route(self, rule, **options):

    def decorator(f):
      self.mound.append((f, rule, options))
      return f

    return decorator

  def register(self, bp, pre_fix=None):
    if pre_fix is None:
      pre_fix = f'/{self.name}'
    for f, rule, options in self.mound:
      endpoint = options.pop('endpoint', self.name + '+' + f.__name__)
      bp.add_url_rule(pre_fix + rule, endpoint, f, **options)
