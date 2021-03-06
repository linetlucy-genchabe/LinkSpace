import os

class Config:
    # UPLOADED_PHOTOS_DEST ='app/static/photos'

    # API_KEY = os.environ.get('API_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Mbuguack@localhost/linkspacedb'

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
     SQLALCHEMY_DATABASE_URI = 'postgresql://zxysbevgknkfxa:128aaa91c3588ef2a9b8c0d9227059c612553bf829bf9cfdcd7664c42da3d673@ec2-54-165-90-230.compute-1.amazonaws.com:5432/ddah81vmv0gm3'

   


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://zxysbevgknkfxa:128aaa91c3588ef2a9b8c0d9227059c612553bf829bf9cfdcd7664c42da3d673@ec2-54-165-90-230.compute-1.amazonaws.com:5432/ddah81vmv0gm3'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
