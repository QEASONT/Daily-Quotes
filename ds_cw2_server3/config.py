import secret
# configuration of app.py
CSRF_ENABLED = True 
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@localhost:3306/dscw2'.format( secret.database_password)
SQLALCHEMY_TRACK_MODIFICATIONS = False
TEMPLATES_AUTO_RELOAD = True
SEND_FILE_MAX_AGE_DEFAULT = 0
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'