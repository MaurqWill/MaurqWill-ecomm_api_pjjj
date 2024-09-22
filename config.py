import os
from dotenv import load_dotenv

# class Config:
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     CACHE_TYPE = 'redis'
#     CACHE_REDIS_URL = os.environ.get('CACHE_REDIS_URL', 'redis://localhost:6379/1')
#     RATELIMIT_STORAGE_URL = os.environ.get('RATELIMIT_STORAGE_URL', 'redis://localhost:6379/0')
#     RATELIMIT_DEFAULT = "3 per day"  # Set default rate limit

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')  # Use simple cache for development
    RATELIMIT_DEFAULT = os.getenv('RATELIMIT_DEFAULT', "100 per day")  # Set default rate limit


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'mysql+mysqlconnector://root:C0dingTemp012!@localhost/bes_ecomm')
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///app.db')
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory SQLite database for testing
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing purposes if using forms

# A dictionary to help in accessing configurations easily
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}




