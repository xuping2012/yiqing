import os
import sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
import logging
from logging import handlers
from conf.settings import LOG_PATH

class Logger(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance: 
            cls.__instance = object.__new__(cls, *args) 
        return cls.__instance 

    def __init__(self):
        self.formater = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(module)s:%(lineno)d ], %(message)s')
        self.logger = logging.getLogger('log')
        self.logger.setLevel(logging.DEBUG)
        self.filelogger = handlers.RotatingFileHandler(LOG_PATH,
                                                       maxBytes=5242880,
                                                       backupCount=3,
                                                       encoding='utf-8')
        # self.console = logging.StreamHandler()
        # self.console.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        # self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        # self.logger.addHandler(self.console)


logger = Logger()

if __name__ == '__main__':
    logger.logger.debug('xxxxxxxxx')
    logger.logger.info('xxxxxxxxxx')

