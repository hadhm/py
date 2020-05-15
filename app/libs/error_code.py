from flask import json, request
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
  code = 500
  error_code = 999
  msg = 'server internal error'
  data = None

  def __init__(self, code=None, error_code=None, msg=None, data=None):
    if code is not None:
      self.code = code
    if error_code is not None:
      self.error_code = error_code
    if msg is not None:
      self.msg = msg
    if data is not None:
      self.data = data
    super(APIException, self).__init__(msg, None)

  def get_body(self, environ=None):
    """Get application/json body."""
    request_head = request.method + ' ' + self.get_request_head()
    dct = {
        'msg': self.msg,
        'code': self.code,
        'error_code': self.error_code,
        'data': self.data,
        'request': request_head,
    }
    return json.dumps(dct)

  def get_headers(self, environ=None):
    """Get a list of headers."""
    return [("Content-Type", "application/json")]

  @staticmethod
  def get_request_head():
    path = str(request.full_path)
    head = path.split('?')
    return head[0]


class Success(APIException):
  code = 200
  msg = 'ok'
  error_code = 0


class AddSuccess(Success):
  code = 201


class DeleteSuccess(Success):
  code = 202
  erro_code = 1


class ServerError(APIException):
  # code = 500
  # msg = server internal error
  # error_code = 999
  pass


class ParameterError(APIException):
  code = 400
  msg = 'invalid parameter'
  error_code = 1000


class NotFoundError(APIException):
  code = 404
  msg = 'not found resource'
  error_code = 1001


class AuthError(APIException):
  code = 401
  msg = 'auth error'
  error_code = 1002
  # 1002 bad token
  # 1003 token expired


class Forbidden(APIException):
  code = 403
  msg = 'forbidden'
  error_code = 1004


class ClientTypeError(APIException):
  code = 400
  msg = "client type error"
  error_code = 1006


class ClientScopeError(APIException):
  code = 400
  msg = 'client scope error'
  error_code = 1007
