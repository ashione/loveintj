"""
Django settings for loveintj project.

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
SECRET_KEY = 'zgfzw))uy!infi1^dws8jyq(4mm7&=7^a2wco-3^lc)%q!0gij'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG =  False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lover',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'loveintj.urls'

WSGI_APPLICATION = 'loveintj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'loveintj',
        'HOST': 'localhost',
        'USER': 'loveintj',
        'PASSWORD': 'tongji',
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
#STATIC_ROOT =os.path.join(os.path.dirname(__file__),'..', 'static').replace('\\','/')
#STATIC_ROOT='/home/vagrant/loveintj/static'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
#STATIC_URL =os.path.join(os.path.dirname(os.path.abspath(__file__)),'..', 'static/')
#STATIC_URL = os.path.join(BASE_DIR,'../static/')
STATIC_URL = '/static/'

STATIC_DIRS = [
    os.path.join(BASE_DIR,"static"),
    os.path.join(BASE_DIR,"loveintj/static"),
    #'/home/vagrant/loveintj/static/',
    #os.path.join(os.path.dirname(__file__),'static'),
 ]

TEMPLATE_DIRS={
        os.path.join(BASE_DIR,'templates/'),
}
#print STATIC_URL
