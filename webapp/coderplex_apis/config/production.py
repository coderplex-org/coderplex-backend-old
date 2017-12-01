import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False
ALLOWED_HOSTS = ['coderplex.org', '*.coderplex.org']
CORS_ORIGIN_WHITELIST = ['coderplex.org', '*.coderplex.org']

#Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

LINKEDIN_CALLBACK_URL = os.environ.get('LINKEDIN_CALLBACK_URL')
GITHUB_CALLBACK_URL = os.environ.get('GITHUB_CALLBACK_URL')
