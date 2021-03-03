# import os
# basedir = os.path.abspath(os.path.dirname(__file__))


# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# class ProdConfig(Config):
#       '''
#     Production configuration child class

#     Args:
#         Config: The parent configuration class with Gen config settings
#     '''
# pass

# class DevConfig(Config):
#       '''
#     Development configuration child class

#     Args:
#         Config: The parent configuration class with Gen config Settings
#     '''
# DEBUG = True

# config_options = {
#     'development' : DevConfig,
#     'production'  : ProdConfig
# }
import os

class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos' 
    # email configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # Simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuaration settings
    '''
    DEBUG = True

class TestConfig(Config):
    '''
    Testing Configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}


