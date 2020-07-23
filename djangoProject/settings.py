"""
Django settings for djangoProject project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = (os.environ['DEBUG_VALUE'] == 'True')

ALLOWED_HOSTS = ['winck-django.herokuapp.com','localhost:8000','localhost']

#Mail Sending
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587


EMAIL_HOST_USER = os.environ['EMAIL_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']
EMAIL_USE_TLS = True
ADMINS = [('Arthur', 'apwinck@gmail.com')]


# Application definition

INSTALLED_APPS = [
    'ckeditor_uploader',
    'ckeditor', 
    'easy_thumbnails',
    'multiselectfield',
    'imoveis',
    'blog',
    'users',
    'location_field.apps.DefaultConfig',
    'django_filters',
    'storages',
    

    #django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'djangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'djangoProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), os.path.join(BASE_DIR, 'fonts')
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

MEDIAFILES_ROOT = os.path.join(BASE_DIR,'media')

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASE_PATH = "static/ckeditor/ckeditor"

#google maps
LOCATION_FIELD_PATH = STATIC_URL + 'location_field'

GOOGLE_MAPS_SECRET_KEY = os.environ['GOOGLE_MAPS']

LOCATION_FIELD = {
    'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    'provider.google.api_key': GOOGLE_MAPS_SECRET_KEY,
}

#s3 AWS STORAGE

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = "winck-django-files"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#whitenoise

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


#SECURITY

CSRF_COOKIE_SECURE = (os.environ['CSRF_COOKIE_SECURE'] == 'True')
SESSION_COOKIE_SECURE = (os.environ['SESSION_COOKIE_SECURE'] == 'True')
SECURE_SSL_REDIRECT = (os.environ['SECURE_SSL_REDIRECT'] == 'True')

#probable bug fix is commenting next line
#django_heroku.settings(locals())