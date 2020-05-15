from flask import Flask as _Flask

from app.libs.json_encoder import JSONEncoder


class Flask(_Flask):
  json_encoder = JSONEncoder
