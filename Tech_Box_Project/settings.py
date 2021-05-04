import os
import sys
from unipath import Path

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://6b5bfc3614f44547a2f28c2c528b4a36@o588927.ingest.sentry.io/5739266",
    integrations=[DjangoIntegration()])

# Build paths inside the project like this: BASE_DIR / 'subdir'.

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = Path(__file__).ancestor(3)
PROJECT_APPS = Path(__file__).ancestor(2)
sys.path.insert(0, Path(PROJECT_APPS, 'apps'))


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ji^#5#f0sqf%4x)&67pdx6k!u0&xlr3^pkdm&rx5%+)46u4v9*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_auth',
    'app_gadgets',
    'crispy_forms',
    'django_celery_beat',
    'rest_framework',
    'rest_framework.authtoken',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Tech_Box_Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'Tech_Box_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

LOGIN_URL = '/'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]

#media
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'vaibhav.thoughtwin@gmail.com'
EMAIL_HOST_PASSWORD = 'vaibhav12345'
EMAIL_USE_SSL = False


# CELERY_BEAT_SCHEDULE = {
#     "scheduled_task":{
#         "task": "app_gadgets.tasks.add",
#         "schedule": 5.0,
#         "args": (10, 5),
#     },
# }

# Cache Settings

# CACHE_MIDDLEWARE_SECONDS = 30

# Database Caching.

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#     }
# }

# File System Caching.

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': r'C:\Users\HP\Desktop\django_1\Tech_Box_Project\cache',
    }
}

# Local Memory Caching.

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     }
# }


# STRIPE PAYMENT INTEGRATION

STRIPE_PUBLIC_KEY = "pk_test_51ImwiJSEWB5q9nyCXg3RCpAHfhxLq9CLmjSl2MfmvJpkX6ceSqi7TUMhRvNbJsPtAwZubGxT9ULpTw3PUct18JB100jKMzbF07"
STRIPE_SECRET_KEY = "sk_test_51ImwiJSEWB5q9nyCQvzOpwmcnW1qCFbeiOtEeU9TBsBaKJvj21udIbgbvIfVGWiOW7PhwHATfH71RIwSexcT4cav00yVsLODqO"
STRIPE_WEBHOOK_SECRET = ""
