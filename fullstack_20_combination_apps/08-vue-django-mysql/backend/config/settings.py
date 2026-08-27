import os
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = os.getenv("DJANGO_DEBUG","False").lower() == "true"
ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = "config.urls"
INSTALLED_APPS = []
MIDDLEWARE = []
TEMPLATES = []
WSGI_APPLICATION = "config.wsgi.application"
DATABASES = {"default": {"ENGINE":"django.db.backends.mysql","NAME":os.environ["MYSQL_DATABASE"],"USER":os.environ["MYSQL_USER"],"PASSWORD":os.environ["MYSQL_PASSWORD"],"HOST":os.environ["MYSQL_HOST"],"PORT":os.environ["MYSQL_PORT"],"OPTIONS":{"connect_timeout":5}}}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
