from flask import Blueprint
from app.api.v1 import (book, user, client, token)


def create_blueprint_v1():
  bp_v1 = Blueprint('v1', __name__, url_prefix='/v1')

  book.api.register(bp_v1, pre_fix='/book')
  user.api.register(bp_v1, pre_fix='/user')

  client.api.register(bp_v1)
  token.api.register(bp_v1)

  return bp_v1
