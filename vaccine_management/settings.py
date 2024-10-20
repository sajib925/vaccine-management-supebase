import os
from pathlib import Path
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent
CORS_ALLOW_ALL_ORIGINS = True



SECRET_KEY = 'django-insecure-8kgg64r&!hz0ay4=j4yiw$e24&qhi7viw%=o*=p@_&!f6b@a@2'

DEBUG = True


ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app"]



INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'doctor',
    'patient',
    'service',
    'contact_us',
    'booking',
    'campaign',
    'review'
]
CSRF_TRUSTED_ORIGINS = [
    'https://vaccine-management-backend-j2ii.onrender.com',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
]


CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://vaccine-management-backend-j2ii.onrender.com",
]
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://vaccine-management-backend-j2ii.onrender.com",
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vaccine_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vaccine_management.wsgi.app'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}





# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres.nlynmffmggnjqqbldrot",
        "PASSWORD": "k._3qU_69e-T2$y",
        "HOST": "aws-0-ap-southeast-1.pooler.supabase.com",
        "PORT": "6543",
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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
