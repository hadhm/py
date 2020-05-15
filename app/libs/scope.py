from app.libs.enums import ClientScopeEnum


class Scope():
  deny_api = []
  allow_api = []
  allow_module = []

  def __add__(self, other):
    self.deny_api = self.deny_api + list(set(other.deny_api))
    self.allow_api = self.allow_api + list(set(other.allow_api))
    self.allow_module = self.allow_module + list(set(other.allow_module))
    return self


class UserScope(Scope):
  allow_api = ['v1.user+get_user']


class AdminScope(Scope):
  allow_module = ['v1.user']

  def __init__(self):
    self + UserScope()


class SuperScope(Scope):

  def __init__(self):
    self + UserScope() + AdminScope()


def is_in_scope(scope, endpoint):
  promise = {
      ClientScopeEnum.USER_SCOPE.value: 'UserScope',
      ClientScopeEnum.ADMIN_SCOPE.value: 'AdminScope',
      ClientScopeEnum.SUPER_SCOPE.value: 'SuperScope',
  }
  scope = globals()[promise[scope]]()

  mod = endpoint.split('+')[0]
  allow = False
  if endpoint in scope.deny_api:
    allow = False
  elif endpoint in scope.allow_api:
    allow = True
  elif mod in scope.allow_module:
    allow = True
  return allow
