from .base import *

SECRET_KEY = "production-secret-key"

DEBUG = False

ALLOWED_HOSTS = [
    "silsila.com",
    "api.silsila.com",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "silsila_prod",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "production-db",
        "PORT": "5432",
    }
}