
'此类输出日志信息'
__author__ = 'ly'

import logging
logging.basicConfig(filename='StockAnalysis.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class MyLog(object):
    def getLoggerByName(self, name):
        return logging.getLogger(name)
