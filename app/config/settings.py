DEBUG = True

SQLALCHEMY_ENGINE = 'cymysql'
SQLALCHEMY_HOST = 'localhost'
SQLALCHEMY_PORT = 3306
SQLALCHEMY_USERNAME = 'root'
SQLALCHEMY_PASSWD = '123456'
SQLALCHEMY_DBNAME = 'py'
SQLALCHEMY_DATABASE_URI = f'mysql+{SQLALCHEMY_ENGINE}://\
{SQLALCHEMY_USERNAME}:{SQLALCHEMY_PASSWD}\
@{SQLALCHEMY_HOST}:{SQLALCHEMY_PORT}/{SQLALCHEMY_DBNAME}'

SQLALCHEMY_TRACK_MODIFICATIONS = True

TOKEN_EXPIRATION = 30 * 24 * 60 * 60

MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = '587'
MAIL_USE_TLS = True
MAIL_USERNAME = '623651795@qq.com'
MAIL_PASSWORD = 'Clsdir1217'
MAIL_DEFAULT_SENDER = '623651795@qq.com'

# ALIDAYU_APP_KEY =
# ALIDAYU_APP_SECRET =
# ALIDAYU_SIGN_NAME =
# ALIDAYU_TEMPLATE_CODE =