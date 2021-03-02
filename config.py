import os


class config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
      '''
    Production configuration child class

    Args:
        Config: The parent configuration class with Gen config settings
    '''
    pass

class DevConfig(Config):
      '''
    Development configuration child class

    Args:
        Config: The parent configuration class with Gen config Settings
    '''
    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production'  : ProdConfig
}


