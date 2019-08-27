import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'g+7!rxl=yycp4i^bo44j+21(ry@sq9fx0-y8$dea1nyemzrtxk'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
