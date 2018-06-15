from .common import *


DEBUG = True

# Allowed host
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dailybread',
        'USER': 'dailybreaduser',
        'PASSWORD': 'dailybreadpass',
        'HOST': 'localhost',
        'PORT': '',

    }
}