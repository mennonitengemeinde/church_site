from pathlib import Path

from environ import Env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env(
    DEBUG=(bool, False),
    SECRET_KEY=(
        str,
        "django-insecure-7l#y#y5f@qulo0&48tt(=&2xbx_69&sb67vmk+a9uh&t_2j833",
    ),
    ALLOWED_HOSTS=(list, ["*"]),
    CSRF_ORIGINS=(list, ["http://localhost:8000"]),
    ADMIN_URL=(str, "admin/"),
    PRODUCTION_DB=(bool, False),
    DB_NAME=(str, "church_db"),
    DB_USER=(str, "daniel"),
    DB_PASS=(str, "password"),
    DB_HOST=(str, "localhost"),
    DB_PORT=(int, 5432),
    CORS_ALLOWED_ORIGINS=(list, []),
    GOOGLE_CLIENT_ID=(str, ""),
    GOOGLE_CLIENT_SECRET=(str, ""),
    SENDGRID_API_KEY=(str, ""),
    DEFAULT_FROM_EMAIL=(str, ""),
    AZURE_ACCOUNT_NAME=(str, ""),
    AZURE_ACCOUNT_KEY=(str, ""),
    AZURE_CONTAINER=(str, ""),
    BOT_API_KEY=(str, ""),
    BOT_URL=(str, ""),
    WOL_EVENTS_BOT_TOKEN=(str, ""),
    WOL_EVENTS_BOT_BASE_URL=(str, ""),
)
Env.read_env(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env("CSRF_ORIGINS")

ADMIN_URL = env("ADMIN_URL")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third party
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "allauth",
    "allauth.account",
    "dj_rest_auth.registration",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "corsheaders",
    "storages",
    # 'compressor',
    # 'crispy_forms',
    # 'crispy_bootstrap5',
    "pwa",
    "django_countries",
    "django_htmx",
    # Project
    "core",
    "accounts.apps.AccountsConfig",
    "churches.apps.ChurchesConfig",
    "speakers.apps.SpeakersConfig",
    "schedules.apps.SchedulesConfig",
    "sermons.apps.SermonsConfig",
    "streams.apps.StreamsConfig",
    "contactus.apps.ContactusConfig",
    "forms.apps.FormsConfig",
    # "telegram.apps.TelegramConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "church_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "church_site.wsgi.application"

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if env("PRODUCTION_DB"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("DB_NAME"),
            "USER": env("DB_USER"),
            "PASSWORD": env("DB_PASS"),
            "HOST": env("DB_HOST"),
            "PORT": env("DB_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Authentication
SITE_ID = 1
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_SESSION_REMEMBER = True
LOGIN_REDIRECT_URL = "/"
SOCIALACCOUNT_AUTO_SIGNUP = False
ACCOUNT_FORMS = {
    "login": "accounts.forms.MgLoginForm",
    "signup": "accounts.forms.MgSignupForm",
}
SOCIALACCOUNT_FORMS = {"signup": "accounts.forms.SMgSignupForm"}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SOCIALACCOUNT_PROVIDERS = {
    #     "APP": {
    #         "client_id": env("GOOGLE_CLIENT_ID"),
    #         "secret": env("GOOGLE_CLIENT_SECRET"),
    #     },
    #     "SCOPE": [
    #         "profile",
    #         "email",
    #     ],
    #     "AUTH_PARAMS": {
    #         "access_type": "online",
    #     },
    # }
}

# Rest
REST_AUTH = {
    "SESSION_LOGIN": True,
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "mg-auth",
    "JWT_AUTH_REFRESH_COOKIE": "mg-refresh-token",
}
# REST_SESSION_LOGIN = True
# REST_USE_JWT = True
# JWT_AUTH_COOKIE = 'mg-auth'
# REFRESH_TOKEN_LIFETIME =

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
else:
    CORS_ALLOWED_ORIGINS = env("CORS_ALLOWED_ORIGINS")

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_USER_MODEL = "accounts.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Toronto"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    },
}

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [BASE_DIR / "assets"]

if DEBUG:
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"

# Send Grid
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = env("SENDGRID_API_KEY")
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

# Azure
AZURE_ACCOUNT_NAME = env("AZURE_ACCOUNT_NAME")
AZURE_ACCOUNT_KEY = env("AZURE_ACCOUNT_KEY")
AZURE_CONTAINER = env("AZURE_CONTAINER")
# AZURE_CUSTOM_DOMAIN = env('AZURE_CUSTOM_DOMAIN', default='')

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# PWA settings
PWA_APP_NAME = "Mennoniten Gemeinde"
PWA_APP_DESCRIPTION = (
    "Here you will find Sermons which could be a blessing for your Spiritual life"
)
PWA_APP_THEME_COLOR = "#602627"
PWA_APP_BACKGROUND_COLOR = "#F4F2F1"
PWA_APP_DISPLAY = "standalone"
PWA_APP_SCOPE = "/"
PWA_APP_ORIENTATION = "any"
PWA_APP_START_URL = "https://mennonitengemeinde.org/"
PWA_APP_STATUS_BAR_COLOR = "default"
PWA_APP_ICONS = [
    {"src": "/static/favicon.ico", "sizes": "96x96 32x32 16x16"},
    {"src": "/static/android-chrome-192x192.png", "sizes": "192x192"},
    {"src": "/static/android-chrome-512x512.png", "sizes": "512x512"},
]
PWA_APP_ICONS_APPLE = [
    {"src": "/static/images/apple_touch_icon.png", "sizes": "180x180"}
]
PWA_APP_SPLASH_SCREEN = [
    {
        "src": "/static/splashscreens/apple-splash-640-1136.jpg",
        "media": "(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)",
    },
    {
        "src": "/static/splashscreens/apple-splash-750-1334.jpg",
        "media": "(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)",
    },
    {
        "src": "/static/splashscreens/apple-splash-1242-2208.jpg",
        "media": "(device-width: 414px) and (device-height: 736px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)",
    },
    {
        "src": "/static/splashscreens/apple-splash-1125-2436.jpg",
        "media": "(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)",
    },
    {
        "src": "/static/splashscreens/apple-splash-1536-2048.jpg",
        "media": "(min-device-width: 768px) and (max-device-width: 1024px) and (-webkit-min-device-pixel-ratio: 2) and (orientation: portrait)",
    },
    {
        "src": "/static/splashscreens/apple-splash-1668-2224.jpg",
        "media": "(min-device-width: 834px) and (max-device-width: 834px) and (-webkit-min-device-pixel-ratio: 2) and (orientation: portrait)",
    },
    {
        "src": "/static/splashscreens/apple-splash-2048-2732.jpg",
        "media": "(min-device-width: 1024px) and (max-device-width: 1024px) and (-webkit-min-device-pixel-ratio: 2) and (orientation: portrait)",
    },
]
PWA_APP_DIR = "ltr"
PWA_APP_LANG = "en-US"

# Bot
BOT_API_KEY = env("BOT_API_KEY")
BOT_URL = env("BOT_URL")

WOL_EVENTS_BOT_TOKEN = ""
WOL_EVENTS_BOT_BASE_URL = ""
