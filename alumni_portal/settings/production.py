from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'

STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))