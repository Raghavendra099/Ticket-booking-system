from pathlib import Path
import os
from dotenv import load_dotenv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Load environment variables from .env file
load_dotenv()

# ----------------- Base Directory -----------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------- Security -----------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "your-fallback-dev-key")  # Use a fallback only in dev
DEBUG = True
ALLOWED_HOSTS = []

# ----------------- Installed Apps -----------------
INSTALLED_APPS = [
    'widget_tweaks',
    'jazzmin',
    'booking',  # Your main app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# ----------------- Middleware -----------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------- URL Configuration -----------------
ROOT_URLCONF = 'ticketproject.urls'

# ----------------- Templates -----------------
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

# ----------------- WSGI -----------------
WSGI_APPLICATION = 'ticketproject.wsgi.application'

# ----------------- Database -----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------- Password Validators -----------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ----------------- Internationalization -----------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------- Static Files -----------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# ----------------- Authentication -----------------
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'booking:login'
LOGOUT_REDIRECT_URL = '/login/'

# ----------------- Stripe Configuration -----------------
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', '')

# ----------------- Email Configuration -----------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.example.com")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD", "")

# ----------------- Jazzmin Settings -----------------
JAZZMIN_SETTINGS = {
    "site_title": "Ticket Booking Admin",
    "site_header": "EasyTicket Admin",
    "site_brand": "EasyTicket",
    "welcome_sign": "Welcome to EasyTicket Admin Portal",
    "copyright": "Your Company",
    "search_model": ["booking.Ticket", "booking.Flight", "booking.Train"],
}

# ----------------- Message Tags -----------------
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# ----------------- Default Auto Field -----------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
