from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['travel-portal-666.herokuapp.com']


DATABASES = {}
DB_URL = os.getenv('DATABASE_URL')
DATABASES['default'] = dj_database_url.config(
    default=DB_URL,
    engine='django.db.backends.postgresql'
)
