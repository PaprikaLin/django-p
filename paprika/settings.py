"""
Django settings for paprika project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from paprika.keys import SECRET_KEY as sk
from paprika.keys import PASSWORD as ps

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = sk

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# !!git push之前修改
#ALLOWED_HOSTS = ['www.paprika0214.icu', 'paprika0214.icu']


ALLOWED_HOSTS = ['192.168.0.105', '127.0.0.1']

# Application definition

# 自定义ckeditor的配置
# CKEDITOR_CONFIGS = {
#     'default': {
#         'width': 'auto',
#         'height': '250px',
#         # tab键转换空格数
#         'tabSpaces': 4,
#         # 工具栏风格
#         'toolbar': 'Custom',
#         # 工具栏按钮
#         'toolbar_Custom': [
#             # 表情 代码块
#             ['Smiley', 'CodeSnippet'],
#             # 字体风格
#             ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
#             # 字体颜色
#             ['TextColor', 'BGColor'],
#             # 链接
#             ['Link', 'Unlink'],
#             # 列表
#             ['NumberedList', 'BulletedList'],
#             # 最大化
#             ['Maximize'],
#         ],
#      # 代码块插件
#      'extraPlugins': ','.join(['codesnippet']),
#     }
# }

INSTALLED_APPS = [
    'mipha',
    'ckeditor',
    'markdown_deux',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'paprika.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'paprika.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': os.path.join(BASE_DIR, 'db.mipha'),
        #'NAME': 'miphapost',
        'NAME': 'django_mipha',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': ps,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = '/website/django-p/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
