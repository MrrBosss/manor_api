from .settings import *
from .settings import env

DEBUG=True

MEDIA_ROOT = "/var/www/manor.itlink.uz/media"
STATIC_ROOT = "/var/www/manor.itlink.uz/static"
SPECTACULAR_SETTINGS["SERVERS"] = [  # noqa: F405
    {"url": "https://manor.itlink.uz", "description": "Manor server"},
]
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'manor',
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DATABASES["default"]["ATOMIC_REQUESTS"] = True
SECRET_KEY = env("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["manor.itlink.uz"])
MEDIA_URL="/media/"
