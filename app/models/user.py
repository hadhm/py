from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import (generate_password_hash, check_password_hash)

from app.models.base_model import BaseModel, db, MixinJSONSerializer
from app.libs.error_code import (
    AuthError,
    ClientScopeError,
)
from app.libs.enums import ClientScopeEnum


class User(BaseModel, MixinJSONSerializer):

  id = Column(Integer, primary_key=True)
  email = Column(String(50), unique=True, nullable=False)
  nickname = Column(String(50), unique=True, nullable=False)
  auth = Column(
      SmallInteger, nullable=False, default=ClientScopeEnum.USER_SCOPE.value)

  _password = Column('password', String(100), nullable=False)

  _exclude = ['create_time', 'status']

  @property
  def password(self):
    return self._password

  @password.setter
  def password(self, raw):
    self._password = generate_password_hash(raw)

  @staticmethod
  def register_by_email(nickname, account, secret):
    with db.auto_commit():
      user = User()
      user.nickname = nickname
      user.email = account
      user.password = secret
      db.session.add(user)
    db.session.flush()

  @staticmethod
  def verify_by_email(mail, password):
    user = User.query.filter_by(email=mail).first_or_404()
    if not check_password_hash(user.password, password):
      raise AuthError()
    return {'uid': user.id, 'auth': user.auth}

  @staticmethod
  def check_auth(auth):
    try:
      auth_enum = ClientScopeEnum(auth)
    except ValueError as e:
      raise ClientScopeError(msg=f'{e}')
    return auth_enum.value
