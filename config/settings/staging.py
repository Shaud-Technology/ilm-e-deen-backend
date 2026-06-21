from .base import *

SECRET_KEY = "staging-secret-key"

DEBUG = False

ALLOWED_HOSTS = [
    "staging.silsila.com",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "silsila_staging",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "staging-db",
        "PORT": "5432",
    }
}