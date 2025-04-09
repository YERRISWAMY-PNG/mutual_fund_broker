import os
from dotenv import load_dotenv

load_dotenv()

# Add to INSTALLED_APPS
INSTALLED_APPS = [

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'users',
    'funds',
]

# Add middleware
MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# CORS settings (adjust in production)
CORS_ALLOW_ALL_ORIGINS = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# RapidAPI settings
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
RAPIDAPI_HOST = 'latest-mutual-fund-nav.p.rapidapi.com'
RAPIDAPI_MF_URL = 'https://latest-mutual-fund-nav.p.rapidapi.com/latest'