import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LINKEDIN_CALLBACK_URL = os.environ.get('LINKEDIN_CALLBACK_URL','http://127.0.0.1:8000/callback')
GITHUB_CALLBACK_URL = os.environ.get('GITHUB_CALLBACK_URL', 'http://127.0.0.1:8000/callback')