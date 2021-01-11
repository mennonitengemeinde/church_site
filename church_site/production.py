from .settings import *
import os

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')
ALLOWED_HOSTS = [os.getenv('WEBSITE_HOSTNAME')] if 'WEBSITE_HOSTNAME' in os.environ else []
ADMIN_URL = os.getenv('ADMIN_URL')

# WhiteNoise configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Add whitenoise middleware after the security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# DBHOST is only the server name, not the full URL
hostname = os.getenv('DB_HOST')

# Configure Postgres database; the full username is username@servername,
# which we construct using the DBHOST value.
if os.getenv('PRODUCTION_DB'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'HOST': hostname,
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASS'),
            'PORT': os.getenv('DB_PORT')
        }
}
