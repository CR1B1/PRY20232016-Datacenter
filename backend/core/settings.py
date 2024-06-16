# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from time import time
from decouple import config
from unipath import Path
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path) # Enviroments vars

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S##ml_pr1342pred23scv84ysdlqwdy14t6765x')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS        = ['*','localhost', 'localhost:85', '127.0.0.1', config('SERVER', default='127.0.0.1')]
CSRF_TRUSTED_ORIGINS = ['http://localhost:85', 'http://127.0.0.1', 'https://' + config('SERVER', default='127.0.0.1'), 'http://127.0.0.1:8000']

# ENV VARS

# Application definition
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    "bootstrap3",
    'crispy_forms',
    'crispy_bootstrap5',
    'dbbackup', # Create database backup
    'public',
    'authentication',
]

AUTH_USER_MODEL = 'authentication.User'
PASSWORD_RESET_TIMEOUT = 3600


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'core.middleware.LoginCheckMiddleWare',
    'core.middleware.AdminCheckMiddleWare',
    'core.middleware.ExceptionMiddleware',
    #HANDLERS MIDDLEWARES

    #'core.middleware.Custom404Middleware',
    #'core.middleware.Custom400Middleware',
    #'core.middleware.Custom500Middleware',
]

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# FOR PRODUCTION ***************************************************************

LOGIN_URL="/login"


ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "login"  # Route defined in authentication/urls.py
LOGOUT_REDIRECT_URL = "login"  # Route defined in authentication/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "templates")  # ROOT dir for templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processor.notification_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Crispy

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = 'bootstrap5'



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

'''DATABASES = {
    "default": 'postgres://admin:root@db:5432/test_db'
}'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': str(os.getenv('NAME_DATABASE')), 
        'USER': str(os.getenv('USER_DATABASE')),
        'PASSWORD': str(os.getenv('PASSWORD_DATABASE')),
        'HOST': str(os.getenv('HOST_DATABASE')), 
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

DATETIME_FORMAT = "%d-%m-%Y %H:%M:%S"

USE_I18N = True

L10N=False

USE_TZ = False

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'static'),
)
MEDIA_URL = '/media/' 
BASE_DIR2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR2, 'media')