### pip install alembic

alembic init alembic
''' 项目中生成 alembic 文件夹，及 alembic.ini
./alembic.ini 中修改：
sqlalchemy.url = mysql+cymysql://root:123456@localhost/py
'''
./alembic/env.py 中修改：
import sys
import os
sys.path = [
os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../'),
*sys.path
]
from demoalembic import Base
target_metadata = Base.metadata
''' 在 flask 下，应该是 import app；然后 target_metadata = app.db.Model.metadata

### alembic 生成迁移文件

alembic revision --autogenerate -m 'message'

### alembic 恢复迁移文件

''' 升级
alembic upgrade head
''' 降级
alembic downgrade

### 清理

数据库中：drop table alembic_version;
rmdir -r ./alembic
alembic init alembic

### 参数

init
revision --autogenerate -m 'message'
upgrade [revision]
downgrade [revision]
heads
history
current
