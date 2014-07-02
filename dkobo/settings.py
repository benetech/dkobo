"""
Django settings for dkobo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# DEBUG is true unless an environment variable is set to something other than 'True'
DEBUG = (os.environ.get('DJANGO_DEBUG', 'True') == 'True')
LIVE_RELOAD = (os.environ.get('DJANGO_LIVE_RELOAD', str(DEBUG)) == 'True')

if not SECRET_KEY and not DEBUG:
    raise ValueError("DJANGO_SECRET_KEY environment variable must be set in production")
elif not SECRET_KEY:
    SECRET_KEY = 'secretShouldBeSetInAnEnvironmentVariable3^*m3xck13'

CSRF_COOKIE_DOMAIN = os.environ.get('CSRF_COOKIE_DOMAIN', None)

if CSRF_COOKIE_DOMAIN:
    SESSION_COOKIE_DOMAIN = CSRF_COOKIE_DOMAIN
    SESSION_COOKIE_NAME = 'kobonaut'

# default in django 1.6+
SESSION_SERIALIZER='django.contrib.sessions.serializers.JSONSerializer'

TEMPLATE_DEBUG = DEBUG

TEMPLATE_LOADERS = (
    'hamlpy.template.loaders.HamlPyFilesystemLoader',
    'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
    )

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'dkobo', 'static'),
    os.path.join(BASE_DIR, 'jsapp'),
    )

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

COMPRESS_ENABLED = str(os.environ.get('COMPRESS_ENABLED', not DEBUG)).lower() == 'true'
COMPRESS_OFFLINE = str(os.environ.get('COMPRESS_OFFLINE', not DEBUG)).lower() == 'true'
COMPRESS_ROOT = os.path.join(BASE_DIR, 'dkobo', 'static')

COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'

COMPRESS_JS_FILTERS = (
    'compressor.filters.yuglify.YUglifyJSFilter',
)
COMPRESS_YUGLIFY_BINARY = 'yuglify'
COMPRESS_YUGLIFY_JS_ARGUMENTS = '--terminal'

GZIP_CONTENT_TYPES = (
    'text/css',
    'application/javascript',
    'text/javascript',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'registration',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dkobo.koboform',
    'compressor',
    'gunicorn',
    'south',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',
)

KOBOCAT_SERVER = os.environ.get('KOBOCAT_SERVER', False)
KOBOCAT_SERVER_PROTOCOL = os.environ.get('KOBOCAT_SERVER_PROTOCOL', 'http')
KOBOCAT_SERVER_PORT = os.environ.get('KOBOCAT_SERVER_PORT', '80')

# The number of surveys to import. -1 is all
KOBO_SURVEY_IMPORT_COUNT = os.environ.get('KOBO_SURVEY_IMPORT_COUNT', 100)

# The number of hours to keep a kobo survey preview (generated for enketo)
# around before purging it.
KOBO_SURVEY_PREVIEW_EXPIRATION = os.environ.get('KOBO_SURVEY_PREVIEW_EXPIRATION', 24)

KOBOFORM_PREVIEW_SERVER = os.environ.get('KOBOFORM_PREVIEW_SERVER', 'http://kf.kobotoolbox.org')
ENKETO_SERVER = os.environ.get('ENKETO_SERVER', 'https://enketo.org')
ENKETO_PREVIEW_URI = os.environ.get('ENKETO_PREVIEW_URI', '/webform/preview')

LOGIN_REDIRECT_URL = '/'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dkobo.urls'

WSGI_APPLICATION = 'dkobo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default="sqlite:///%s/db.sqlite3" % BASE_DIR)
}

ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# For GeoDjango heroku buildpack
GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH')
GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')
POSTGIS_VERSION = (2, 0, 3)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'django.kobo@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'djkobo2013!')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


SITE_ID = os.environ.get('DJANGO_SITE_ID', None)

ACCOUNT_ACTIVATION_DAYS = 3
LOGIN_REDIRECT_URL = '/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': [],
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

# Djangular

APPEND_SLASH = False

# -------------------------------------------

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ]
}
