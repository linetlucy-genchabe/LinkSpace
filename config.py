import os

class Config:
    # UPLOADED_PHOTOS_DEST ='app/static/photos'

    # API_KEY = os.environ.get('API_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lynne:lynne2022@localhost/linkspacedb'

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
   # simple mde configuration
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

     #mail cconfiguration


    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS=True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD= os.environ.get("MAIL_PASSWORD")
    


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lynne:lynne2022@localhost/linkspacedb'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
