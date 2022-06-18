"""
Django settings for clg_classifieds project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6sk4g74)(sltc3%2g4w0nf04m6d_==sjkq6&4!opix4paf1&=w'
GOOGLE_RECAPTCHA_SECRET_KEY = '6LdG5RYgAAAAAKxSv1XKO8cKPtuafDoBuyipySg1'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'clg_classifieds.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Templates'],
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

WSGI_APPLICATION = 'clg_classifieds.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'NAME': 'clg_classfields',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'hp1234',
        'HOST': 'localhost', 
    }
}
Access Key ID:
AKIA5JPXNPPJOVPLGN64
Secret Access Key:
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

'''
DATABASES = {
    'default': {
        'NAME': 'clg_classfields',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'admin',
        'PASSWORD': '9131285337',
        'HOST': 'database-1.cenwprx98qyc.us-east-1.rds.amazonaws.com', 
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_TZ = True






EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'aroramanav886@gmail.com'
EMAIL_HOST_PASSWORD = 'hpgwkczwxefdyqom'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets"),
    )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#S3 BUCKETS CONFIG

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = 'AKIA5JPXNPPJPHKGLNVY'

AWS_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = 'collegekart'

AWS_QUERYSTRING_AUTH = False
