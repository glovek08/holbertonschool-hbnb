import os
from urllib.parse import quote_plus


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = False


class DevelopmentConfig(Config):
    RESTX_VALIDATE = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(
        os.getenv("DB_USER", "pizza"),
        quote_plus(os.getenv("DB_PASSWORD", "Pizza123@@")),
        os.getenv("DB_HOST", "localhost"),
        os.getenv("DB_PORT", "3306"),
        os.getenv("DB_NAME", "hbnb_v1"),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {"development": DevelopmentConfig, "default": DevelopmentConfig}
