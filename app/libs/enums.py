from enum import Enum


class ClientTypeEnum(Enum):
  USER_EMAIL = 100
  USER_MOBILE = 101

  USER_MINA = 200
  USER_WX = 201


class ClientScopeEnum(Enum):
  USER_SCOPE = 1
  ADMIN_SCOPE = 2
  SUPER_SCOPE = 3
