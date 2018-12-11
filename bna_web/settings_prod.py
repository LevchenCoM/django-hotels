DEBUG = False
ALLOWED_HOSTS = ['*']

FILE_UPLOAD_PERMISSIONS = 0o644

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bna_db',
        'USER': 'bna_site',
        'PASSWORD': 'MightyBogdan',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}
