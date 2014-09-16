class Config(object):
    DEBUG = False
    TESTING = False

class Development(Config):
    MODE='DEVELOPMENT'
    DEBUG = True
    DATABASE = 'development_db'
    DEST_MAIL='martin.mantovani@gmail.com'
    LOG_INFO_FILE='/tmp/billetera_info.log'
    LOG_ERROR_FILE='/tmp/billetera_error.log'


class Testing(Config):
    MODE='TESTING'
    DEBUG = True
    DATABASE = 'development_db'
    DEST_MAIL='martin.mantovani@gmail.com'
    LOG_INFO_FILE='/tmp/billetera_info.log'
    LOG_ERROR_FILE='/tmp/billetera_error.log'

class Production(Config):
    MODE='PRODUCTION'
    DATABASE = 'production_db'
    LOG_INFO_FILE='/tmp/billetera_info.log'
    LOG_ERROR_FILE='/tmp/billetera_error.log'
    DEST_MAIL='martin.mantovani@gmail.com'


