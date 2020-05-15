from wtforms import Form
from flask import request

from app.libs.error_code import ParameterError


class BaseForm(Form):

  # 改写__init__，使其默认从request.json中取值
  def __init__(self):
    # 同时支持get, post
    # 防止Content-Type为application/json时出错，silent
    content = request.headers.get("Content-Type")
    if content == 'application/json':
      data = request.json
    elif content == 'application/x-www-form-urlencoded' or 'multipart/form-data':
      # request.form is ImmutableMulitDict
      data = request.form.to_dict()
    else:
      data = request.get_json(silent=True)
    args = request.args.to_dict()
    print(data, args)
    super(BaseForm, self).__init__(data=data, **args)

  # 默认valid没通过触发ParameterError，将Form.errors写入msg
  def validate_for_api(self):
    valid = super(BaseForm, self).validate()
    if not valid:
      raise ParameterError(msg=self.errors)
    return self
