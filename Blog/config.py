import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECURE_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIN_SENDER = 'Flasky Admin<>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopConfig:
    pass


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopConfig
}
