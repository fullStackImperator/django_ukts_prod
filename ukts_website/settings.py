"""
Django settings for ukts_website project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-98li_w!@*l#he&17&r@g&p16=h^lao8k+b-m$9$($+o9koui!s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.2', '127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'blog.apps.BlogConfig',
    # 'treneri',
    'orderable',
    'crispy_forms',
    'taggit',
    'django.contrib.postgres',
    'ckeditor',
    'ckeditor_uploader',
    'treneri.apps.TreneriConfig',
    'magazin.apps.MagazinConfig',
    'klinike.apps.KlinikeConfig',
    'edukacija.apps.EdukacijaConfig',
    'onama.apps.OnamaConfig',
    'imagekit',
    'zatrenere.apps.ZatrenereConfig',
    'phonenumber_field',
    'django_countries',

    'storages'
]


TAGGIT_CASE_INSENSITIVE = True

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#ckeditor upload path
CKEDITOR_UPLOAD_PATH="uploads/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ukts_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'ukts_website.wsgi.application'


CSRF_COOKIE_DOMAIN = None

CSRF_TRUSTED_ORIGINS = [
    'https://ukts-website.herokuapp.com'
]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'blog',
        'USER': 'blog',
        'PASSWORD': 'Stanford',
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



LOGIN_REDIRECT_URL = 'treneri:treneri_list' 
LOGIN_URL = 'account:login'
# LOGOUT_URL = 'post_list'
LOGOUT_REDIRECT_URL = 'blog:post_list'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Belgrade' # 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     'django_plotly_dash.finders.DashAssetFinder',
#     'django_plotly_dash.finders.DashComponentFinder',
#     'django_plotly_dash.finders.DashAppDirectoryFinder',
# ]

# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_LOCATION = 'static'
# STATICFILES_DIRS = [
#     BASE_DIR / 'static'
# ]

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# VENV_PATH = os.path.dirname(BASE_DIR)


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR /"media/"


# S3 configuration
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = 'public-read'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AWS_S3_ACCESS_KEY_ID = 'AKIAW5FRUHHA72EAPMOY'
AWS_S3_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = 'ukts-demo'



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


#SMTP Configuration
DEFAULT_FROM_EMAIL = 'stvel075@gmail.com'

EMAIL_Backend = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'stvel075@gmail.com'
EMAIL_HOST_PASSWORD = 'xxx'


CKEDITOR_CONFIGS = {
    'default': {
     
        # 'skin': 'moono',
        # # 'skin': 'office2013',
        # 'toolbar_Basic': [
        #     ['Source', '-', 'Bold', 'Italic']
        # ],
        'toolbar_Custom': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Youtube','Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['CodeSnippet']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
            ]},
        ],
        'toolbar': 'Custom',  # put selected toolbar config here
        'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        'height': 400,
        # 'width': '100%',
        'filebrowserWindowHeight': 725,
        'filebrowserWindowWidth': 940,
        'toolbarCanCollapse': True,
        'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'codesnippet',
        ]),
    }
}


import django_heroku
django_heroku.settings(locals())