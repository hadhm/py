from flask import current_app
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error_code import (APIException, ServerError)

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
  if isinstance(e, APIException):
    return e
  elif isinstance(e, HTTPException):
    code = e.code
    msg = e.description
    error_code = 2000
    return ServerError(code, error_code, msg)
  else:
    if current_app.config['DEBUG']:
      tb_frame = e.__traceback__.tb_frame
      tb_lineno = e.__traceback__.tb_lineno
      tb_next = e.__traceback__.tb_next
      while tb_next is not None:
        tb_frame = tb_next.tb_frame
        tb_lineno = tb_next.tb_lineno
        tb_next = tb_next.tb_next
      return ServerError(msg='{}({}) : {}'.format(
          tb_frame.f_globals["__file__"], tb_lineno, e))
    else:
      return ServerError(msg=f'{e}')


if __name__ == '__main__':
  #
  app.run(host='0.0.0.0')
