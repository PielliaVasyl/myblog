__author__ = 'Piellia Vasyl'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'vrevjoD3Ffek'


import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['pellia@ukr.net']

# pagination
POSTS_PER_PAGE = 3
