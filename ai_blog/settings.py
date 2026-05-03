"""
Django settings for ai_blog project.
"""
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Read .env file manually
def get_env(key, default=None):
    value = os.environ.get(key)
    if value is None:
        try:
            with open(BASE_DIR / '.env') as f:
                for line in f:
                    if line.strip() and not line.startswith('#'):
                        parts = line.strip().split('=', 1)
                        if len(parts) == 2 and parts[0].strip() == key:
                            return parts[1].strip()
        except:
            pass
    return value if value is not None else default

SECRET_KEY = get_env('SECRET_KEY', 'django-insecure-ai-blog-secret-key-1234567890')
DEBUG = get_env('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']  # Allow all hosts for Vercel deployment

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'posts',
    'ai_features',
    'dashboard',
    'ckeditor',
    'ckeditor_uploader',
    'taggit',
    'crispy_forms',
    'crispy_tailwind',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ai_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ai_blog.wsgi.application'

# Database configuration - use SQLite for development, PostgreSQL for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Check if using PostgreSQL (for Vercel Postgres)
db_url = get_env('DATABASE_URL')
if db_url:
    import dj_database_url
    DATABASES['default'] = dj_database_url.parse(db_url, conn_max_age=600)

AUTH_USER_MODEL = 'users.CustomUser'
CRISPY_TEMPLATE_PACK = "tailwind"

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# For Vercel - disable session persistence issues
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
    },
}
CKEDITOR_UPLOAD_URL = '/ckeditor/upload/'
CKEDITOR_BROWSE_URL = '/ckeditor/browse/'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_HTTPONLY = False
