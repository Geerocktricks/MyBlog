import os

class Config:
    '''
    This is the main configuration class for the app
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCEMY_DATABASE_URI = 'postgresql+psycopg2://Geerocktricks:Geerock_1@localhost/MyBlog'


class ProdConfig(Config):
    '''
    This is the production confiuration that inherits from the main Config class
    '''
    pass


class DevConfig(Config):
    '''
    This is the Dev configurations that inherits from the main config class
    '''
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
