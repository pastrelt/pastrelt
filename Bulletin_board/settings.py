"""
Django settings for Bulletin_board project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-##iigrm(=#n&b++hyrzmos!b9@3!_6pfsj#%$(8lx)=v$8xrwj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Регистрация и аутентификация.
    'sign',
    'protect',

    # Настройки под allauth.
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Рабочий проект.
    'bulletin'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Добавил по причине ошибки при миграции данных в модуле D8 урок 4.
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'Bulletin_board.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Это верная настройка 'DIRS' не троать!
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # `allauth` needs this from django
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = [

    # Отключил вход в систему по имени пользователя в администраторе Django, независимо от `allauth`.
    'django.contrib.auth.backends.ModelBackend',

    # Cпециальные методы аутентификации `allauth`, такие как вход по электронной почте.
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'Bulletin_board.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# После этого, когда пользователь попытается получить доступ к защищенной странице без аутентификации,
# он будет перенаправлен на страницу входа, указанную в переменной LOGIN_URL.
# Конкретизация URL-адреса, на котором находится страница аутентификации,
# а также страница, на которую перенаправляется пользователь после успешного входа на сайт,
# в данном случае корневая страница сайта.
#LOGIN_URL = 'accounts/login/'
#LOGIN_URL = 'sign/login/'
LOGIN_URL = 'sign/register/'
LOGIN_REDIRECT_URL = '/'


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо формы по умолчанию,
# необходимо добавить строчку в файл настроек проекта settings.py:
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

# Настройки для отправки писем.
EMAIL_HOST = 'smtp.yandex.ru'  # Адрес сервера Яндекс-почты для всех один и тот же.
EMAIL_PORT = 465  # Порт smtp сервера тоже одинаковый.
EMAIL_HOST_USER = 'passtreltsov'  # Имя почтовоого ящика ( до собаки ) отправителя.
EMAIL_HOST_PASSWORD = 'uzsjmibnpkxffmyf'  # Пароль от почты.
EMAIL_USE_SSL = True  # Яндекс использует ssl.

# Здесь указываем уже свою ПОЛНУЮ почту, с которой будут отправляться письма.
DEFAULT_FROM_EMAIL = 'passtreltsov@yandex.ru'
