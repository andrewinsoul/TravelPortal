from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'PORT': os.getenv('DB_PORT'),
        'HOST': os.getenv('DB_HOST'),
        'TEST': {
            'CHARSET': None,
            'COLLATION': None,
            'NAME': 'test.db',
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': 'postgres',
            'PORT': 5432,
            'USER': 'postgres',
            'MIRROR': None
        }

    }
}
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (('staticfiles'),)
STATIC_URL = '/staticfiles/admin/'
print('>>>>>>>>>>> ', STATIC_ROOT)
