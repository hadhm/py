### pip install flask-migrate

from py import app
from app.models.base_model import db

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

### 使用

''' 初始化数据库
python demomigrate.py db init
''' 生成 migrations 文件夹

''' 生成迁移脚本
python demomigrate.py db migrate

''' 修改真实的数据库
python demomigrate.py db upgrade

### 使用 script、migrate 可以取代的 alembic 的繁杂调用
