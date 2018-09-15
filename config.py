import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('RUNLOG_SECRET_KEY')
    MAIL_SERVER = os.environ.get('RUNLOG_MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('RUNLOG_MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('RUNLOG_MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('RUNLOG_MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('RUNLOG_MAIL_PASSWORD')
    RUNLOG_MAIL_SUBJECT_PREFIX = '[Runlog]'
    RUNLOG_MAIL_SENDER = 'Runlog Admin <runlog@example.com>'
    RUNLOG_ADMIN = os.environ.get('RUNLOG_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('RUNLOG_DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'runlog-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('RUNLOG_TEST_DATABASE_URL') or \
        'sqlite://' + os.path.join(basedir, 'runlog-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('RUNLOG_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'runlog.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}