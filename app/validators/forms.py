from wtforms import StringField, IntegerField
from wtforms.validators import (DataRequired, length, ValidationError, Email,
                                Regexp)

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
  account = StringField(validators=[DataRequired(), length(min=2, max=50)])
  secret = StringField()
  client_type = IntegerField(validators=[
      DataRequired(),
  ])

  def validate_client_type(self, value):
    try:
      if type(value.data) == str:
        value.data = int(value.data)
      client = ClientTypeEnum(value.data)
    except ValueError as e:
      raise e
    self.client_type.data = client


class ClientEmailForm(ClientForm):
  account = StringField(validators=[length(max=50), Email()])
  secret = StringField(validators=[Regexp(r'^[A-Za-z0-9&*#@]{4,50}')])
  nickname = StringField(validators=[DataRequired(), length(min=2, max=50)])

  def validate_account(self, val):
    if User.query.filter_by(email=val.data).first():
      raise ValidationError(message='duplicate email')

  def validate_nickname(self, val):
    if User.query.filter_by(nickname=val.data).first():
      raise ValidationError(message='duplicate nickname')
