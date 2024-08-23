class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:rootuser@localhost/bes_ecomm'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True