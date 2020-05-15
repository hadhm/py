from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

from app.libs.redprint import Redprint
from app.validators.forms import ClientForm
from app.libs.enums import (ClientTypeEnum, ClientScopeEnum)
from app.libs.error_code import (Success, Forbidden)
from app.models.user import User

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
  # 前端校验
  form = ClientForm().validate_for_api()
  # 后端校验
  promise = {ClientTypeEnum.USER_EMAIL: User.verify_by_email}
  # 后端校验 - 检查帐号、密码
  identity = promise[form.client_type.data](
    form.account.data, form.secret.data)
  # 后端校验 - 检查scope
  scope = User.check_auth(identity['auth'])
  #
  expiration = current_app.config['TOKEN_EXPIRATION']
  token = generate_auth_token(
    identity['uid'], form.client_type.data, scope, expiration)
  return Success(data={'token': token.decode('utf8')})


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
  s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
  print(uid, ac_type.value, scope)
  return s.dumps({
    'uid': uid,
    'ac_type': ac_type.value,
    'scope': scope
  })
