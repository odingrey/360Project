"""
Django settings for soda project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from photologue import PHOTOLOGUE_APP_DIR

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import site_logging
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
AUTH_PROFILE_MODULE = 'project.userprofile'

#LOGIN_REDIRECT_URL = 'django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = '/slowergram'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ojq@xis6i5rj_zzgtmps3#p^ju&lm0$znblh1xb1+#8dcv!2r%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
SITE_ID = 1


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'south',
    'project',
    'sortedm2m',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASE_PATH = os.path.join(PROJECT_ROOT, 'slowergram.db')
# DATABASE_PATH = os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


# Directories
#PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = BASE_DIR + '/project/media/'
MEDIA_URL = '/media/'
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#)



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = (BASE_DIR + '/project/static') 
STATIC_URL = '/slowergram/static/'
STATICFILES_DIRS = ( os.path.join(PROJECT_ROOT,'static'),)

SOUTH_MIGRATION_MODULES = {
    'photologue': 'photologue.south_migrations',
}

