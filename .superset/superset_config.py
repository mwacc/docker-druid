import os

#CACHE_CONFIG = {
#    'CACHE_TYPE': 'redis',
#    'CACHE_DEFAULT_TIMEOUT': 300,
#    'CACHE_KEY_PREFIX': 'superset_',
#    'CACHE_REDIS_HOST': 'redis',
#    'CACHE_REDIS_PORT': 6379,
#    'CACHE_REDIS_DB': 1,
#    'CACHE_REDIS_URL': 'redis://redis:6379/1'}
SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://superset:superset@postgres:5432/superset'

LOG_FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
LOG_LEVEL = 'DEBUG'
ENABLE_TIME_ROTATE = False
TIME_ROTATE_LOG_LEVEL = 'DEBUG'
FILENAME = os.path.join('/var/log/superset', 'superset.log')
ROLLOVER = 'midnight'
INTERVAL = 1
BACKUP_COUNT = 30
#SECRET_KEY = 'thisISaSECRET_1234'
