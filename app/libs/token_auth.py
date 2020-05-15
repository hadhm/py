from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import (JSONWebSignatureSerializer as Serializer,
                          SignatureExpired, BadSignature)

from app.libs.error_code import (AuthError, Forbidden)
from app.libs.scope import is_in_scope

User = namedtuple('User', ['uid', 'ac_type', 'scope'])

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(account, password):
  user = verify_token(account)
  if not user:
    return False
  else:
    g.user = user
    return True


def verify_token(token):
  s = Serializer(current_app.config['SECRET_KEY'])
  try:
    data = s.loads(token)
  except BadSignature:
    raise AuthError(msg='bad token', error_code=1002)
  except SignatureExpired:
    raise AuthError(msg='token expired', error_code=1003)
  #
  if not is_in_scope(data['scope'], request.endpoint):
    raise Forbidden()
  #
  uid = data['uid']
  ac_type = data['ac_type']
  scope = data['scope']
  return User(uid, ac_type, scope)
