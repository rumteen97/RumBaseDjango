from pathlib import Path
from environs import Env

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
env = Env()
env.read_env()

# LANGUAGE_CODE = "fa-IR"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
USE_L10N = True
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "users.User"
X_FRAME_OPTIONS = "SAMEORIGIN"

LANGUAGES = [
    # ('fa', 'Persian'),
    ('en', 'English'),
]

LOCALE_PATHS = [
    str(BASE_DIR / "locale"),
]

STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_DIR / "collected_statics")
STATICFILES_DIRS = [str(BASE_DIR / "static")]

MEDIA_ROOT = str(BASE_DIR / "media")
MEDIA_URL = "/media/"

SECRET_KEY = env.str("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])
APPEND_SLASH = True

INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    # "unfold.contrib.import_export",  # optional, if django-import-export package is used
    # "unfold.contrib.guardian",  # optional, if django-guardian package is used
    # "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    # "unfold.contrib.location_field",  # optional, if django-location-field package is used
    # "unfold.contrib.constance",  # optional, if django-constance package is used
    # "unfold.contrib.hijack",  # optional, if django-hijack package is used

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',

    'auditlog',  # required for django-auditlog
    'django_filters',  # required for django-filter
    'rest_framework',  # required for djangorestframework

    'dj_control_room_base',  # Required: shared core library (provides dcr_icons template tags and design system)
    'dj_redis_panel',  # If you installed [redis]
    'dj_cache_panel',  # If you installed [cache]
    'dj_urls_panel',  # If you installed [urls]
    'dj_celery_panel',  # If you installed [celery]
    'dj_signals_panel',  # If you installed [signals]
    'dj_control_room',  # Django Control Room (list after panels so they appear in one section)

    'django_celery_beat',

    'apps.core',
    'apps.users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "auditlog.middleware.AuditlogMiddleware",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR / "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                "django.template.context_processors.i18n",
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DATABASE_NAME"),
        "USER": env.str("DATABASE_USER"),
        "PASSWORD": env.str("DATABASE_PASSWORD"),
        "HOST": env.str("DATABASE_HOST"),
        "PORT": env.str("DATABASE_PORT"),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env.str("REDIS_LOCATION", default="redis://127.0.0.1:6379/"),
        "OPTIONS": {
            "SOCKET_CONNECT_TIMEOUT": 5,  # seconds
            "SOCKET_TIMEOUT": 5,  # seconds
        }
    }
}

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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

AUDITLOG_INCLUDE_ALL_MODELS = True
AUDITLOG_USE_BASE_MANAGER = True
AUDITLOG_STORE_JSON_CHANGES = True

UNFOLD = {
    "SITE_TITLE": "Rum Admin",
    "SITE_HEADER": "Rum Django Admin",
    "SITE_SUBHEADER": "Rum Django Admin",
    "SITE_VERSION": "0.0.0",
    "SHOW_BACK_BUTTON": True,  # show/hide "Back" button on changeform in header, default: False
    "SHOW_UI_WARNINGS": True,  # show/hide warnings in UI, default: False
}
