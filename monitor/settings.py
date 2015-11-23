"""
Django settings for monitor project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from mongoengine import connect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^uhnr%8t)&o49jfq_m09@w=h7m90^$b01j(4li&1#w9mb#iwdy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # custom youself user
    # 'mongoengine.django.mongo_auth',

    'program',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'monitor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # django filesystem: django.template.loaders.filesystem.Loader
        'DIRS': [
            os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates').replace('\\', '/'),
        ],
        'APP_DIRS': True,  # app_directories: django.template.loaders.app_directories.Loader
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.csrf',

                # there add `pagination` app(third packages) to CONTEXT_PROCESSORS
                # #### 'django.template.context_processors.auth',
                # 'django.template.context_processors.debug',
                # 'django.template.context_processors.i18n',
                # 'django.template.context_processors.media',
                # 'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'monitor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

    # 'default': {
    #     'ENGINE': 'django_mongodb_engine',
    #     'NAME': 'ada',
    # }
}

# AUTH_USER_MODEL = 'mongo_auth.MongoUser'
# SESSION_ENGINE = 'mongoengine.django.sessions'
MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'
AUTHENTICATION_BACKENDS = ('mongoengine.django.auth.MongoEngineBackend', )


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

FILE_CHARSET = 'utf-8'
DEFAULT_CHARSET = 'utf-8'


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# template tag `static`, if you use yourself staticfiles file, like as css,
# you should add `STATICFILES_DIRS` variable in settings files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
)


# setting mongodb
# connect('ada', host='192.168.250.200', port=27017)
# connect('ada', host='localhost', port=27017)
connect('ada', host='192.168.0.223', port=27017)
