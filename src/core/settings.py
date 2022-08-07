from pathlib import Path

from corsheaders.defaults import default_methods, default_headers
from environ import Env

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
Env.read_env()

SECRET_KEY = env
DEBUG = env.bool(var="DEBUG")
ALLOWED_HOSTS = ("*",)
INSTALLED_APPS = (
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third Library apps
    "corsheaders",
    "django_filters",
    "rest_framework",
    # Project apps
    "news",
)
MIDDLEWARE = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)
ROOT_URLCONF = "core.urls"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
TEMPLATES = (
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (),
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
)
WSGI_APPLICATION = "core.wsgi.application"
ASGI_APPLICATION = "core.asgi.application"
DATABASES = {"default": env.db()}

AUTH_PASSWORD_VALIDATORS = (
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
)

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKEND": (
        "django_filters.rest_framework.DjangoFilterBackend",
    )
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = default_methods
CORS_ALLOW_HEADER = default_headers
CORS_ALLOW_CREDENTIALS = True

CELERY_BROKER_URL = env.str(var="CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env.str(var="CELERY_RESULT_BACKEND")

X_FINHUB_TOKEN = env.str(var="X_FINHUB_TOKEN")
