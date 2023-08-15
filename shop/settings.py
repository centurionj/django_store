import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
# jazzmin необходимо установить на первое место,
# чтоб джазмин перекрыл встроенную админку

    'jazzmin',

    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'mptt',
    'rest_framework',
    'captcha',

    'aut',
    'cart',
    'favourites',
    'main',
    'news',
    'orders',
    'products',
    'promocodes',
    'setups',
    'static',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'main.context_processors.header',
                'cart.context_processors.cart_context',
                'favourites.context_processors.favourite_context',
                'setups.context_processors.setup',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Password validation

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Vladivostok'

USE_I18N = True

USE_TZ = True


# JAZZMIN

JAZZMIN_SETTINGS = {
    'site_title': 'Админка',
    'site_header': 'Админка',
    'site_brand': 'Админка',
    'show_sidebar': True,
    'navigation_expanded': False,
    'hide_apps': ['aut'],
    'hide_models': [],
    'related_modal_active': True,
    'custom_css': None,
    'custom_js': None,
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# для mixins

LOGIN_URL = 'login'

# Настройки для сессии

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_NAME = 'my_session'
SESSION_COOKIE_AGE = 30 * 24 * 3600  # для админки
SESSION_EXPIRE_SECONDS = 3600  # для обычных пользователей
SESSION_COOKIE_SECURE = False  # для использования HTTPS (True)
SESSION_COOKIE_HTTPONLY = True  # закрыл доступ к cookie через JS
SESSION_SAVE_EVERY_REQUEST = True  # для сохранения сессии при перемещении на сайте
SESSION_COOKIE_SAMESITE = 'Lax'

# Настройки электронной почты

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# настройки google recaptcha v2

RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')

# настройки Chat-GPT

GPT_API_KEY = os.getenv('GPT_API_KEY')

# redis

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

# celery

CELERY_BROKER_URL = 'redis://{}:{}'.format(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))
CELERY_RESULT_BACKEND = 'redis://{}:{}'.format(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))
CELERY_IMPORTS = ('aut.tasks', 'products.tasks.tasks', 'news.tasks', 'orders.tasks')
