import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:C0dingTemp012!@localhost/bes_ecomm'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///app.db'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = False

# class TestingConfig(Config):
#     """Testing configuration."""
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use in-memory database for tests
#     DEBUG = True
#     # WTF_CSRF_ENABLED = False  # Disable CSRF for testing







# import os

# class DevelopmentConfig:
#     SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:C0dingTemp012!@localhost/bes_ecomm'
#     CACHE_TYPE = 'SimpleCache'
#     DEBUG = True
#     TESTING = False
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# class ProductionConfig:
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///app.db'
#     CACHE_TYPE = 'SimpleCache'
#     DEBUG = False
#     TESTING = False
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# class TestingConfig:
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory SQLite database for testing
#     CACHE_TYPE = 'SimpleCache'
#     DEBUG = True
#     TESTING = True
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     WTF_CSRF_ENABLED = False  # Disable CSRF for testing purposes if using forms

# # A dictionary to help in accessing configurations easily
# config_by_name = {
#     'development': DevelopmentConfig,
#     'production': ProductionConfig,
#     'testing': TestingConfig
# }
