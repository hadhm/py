from flask import g

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.libs.error_code import (Success, DeleteSuccess)
from app.models.base_model import db
from app.models.user import User

api = Redprint('user')


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
  user = User.query.filter_by(id=g.user.uid).first_or_404()
  # return jsonify(dict(user))
  return Success(data=user)


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
  user = User.query.filter_by(id=uid).first_or_404()
  # return jsonify(dict(user))
  return Success(data=user)


@api.route('', methods=['PUT'])
def update_user():
  return 'update user'


@api.route('', methods=['DELETE'])
@auth.login_required
def delte_user():
  uid = g.user.uid
  with db.auto_commit():
    user = User.query.filter_by(id=uid).first_or_404()
    user.delete()
    return DeleteSuccess(data=user)


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delte_user(uid):
  with db.auto_commit():
    user = User.query.filter_by(id=uid).first_or_404()
    user.delete()
    return DeleteSuccess(data=user)
