DEBUG = False
ALLOWED_HOSTS = ['*']

FILE_UPLOAD_PERMISSIONS = 0o644

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}
