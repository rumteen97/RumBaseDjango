from config.settings.base import *

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

INTERNAL_IPS = [
    "127.0.0.1",
]

CORS_ALLOW_ALL_ORIGINS = True
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
CSRF_TRUSTED_ORIGINS = ['http://*', 'https://*']
ALLOWED_HOSTS = ['*']
DEBUG = True
