# -*- coding: utf-8 -*-
'日志输出'
__author_ = 'ly'


import logging
import logging.handlers
import Common
import ConfigManegment

class LogInfo(object):
    _logger = None

    def __init__(self):


        logPath = ConfigManegment.ConfigManegment().getLogPath()
        fh = logging.FileHandler(logPath)
        if Common.LogLevel.DEUBG_LOG.value == ConfigManegment.ConfigManegment().getLogLevel():
            fh.setLevel(logging.DEBUG)
        else:
            fh.setLevel(logging.INFO)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self._logger = logging.getLogger('StockLog')

        if not self._logger.handlers:
            self._logger.addHandler(fh)
            #配置文件暂时不生效，这里先用代码处理
            #日志等级DEBUG>INFO>WARNING>ERROR
            self._logger.setLevel(logging.DEBUG)



    #DEBUG>INFO>WARNING>ERROR
    def debugLog(self, msg):
        self._logger.debug(msg)
    def infoLog(self, msg):
        self._logger.info(msg)


if __name__ == '__main__':
    '''l = LogInfo()
    l.debugLog('ddddd')
    l.infoLog('inininin')'''
    pass

