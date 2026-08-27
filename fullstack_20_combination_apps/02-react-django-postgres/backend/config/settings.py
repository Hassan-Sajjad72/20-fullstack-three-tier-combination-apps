import os
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = os.getenv("DJANGO_DEBUG","False").lower() == "true"
ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = "config.urls"
INSTALLED_APPS = []
MIDDLEWARE = []
TEMPLATES = []
WSGI_APPLICATION = "config.wsgi.application"
DATABASES = {"default": {"ENGINE":"django.db.backends.postgresql","NAME":os.environ["DB_NAME"],"USER":os.environ["DB_USER"],"PASSWORD":os.environ["DB_PASSWORD"],"HOST":os.environ["DB_HOST"],"PORT":os.environ["DB_PORT"]}}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
