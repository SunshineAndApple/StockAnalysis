# -*- coding: utf-8 -*-
'此类负责加载配置文件和获取配置文件中的参数'
__author__ = 'ly'

import os
import configparser

class ConfigManegment(object):
    _searchStep = None
    _targetFolderPath = None

    _logPath = None
    _logLevel = None

    def __init__(self):
        self.readConfigFile()

    def readConfigFile(self):
        conf = configparser.ConfigParser()
        conf.read(os.getcwd()+'\\cfg.ini')
        self._searchStep = conf.get('Serach Step', 'len')
        self._targetFolderPath = conf.get('Target Path', 'path')

        self._logPath = conf.get('Log Config', 'logpath')
        self._logLevel = conf.get('Log Config', 'level')

        #print(self._searchStep)
        #print('path %s' % self._targetFolderPath)
        #print(self._logPath)
        #print(self._logLevel)


    def getSearchStep(self):
        return self._searchStep

    def getTargetFolderPath(self):
        return self._targetFolderPath

    def getLogPath(self):
        return self._logPath

    def getLogLevel(self):
        return self._logLevel

if __name__ == '__main__':
    ConfigManegment().readConfigFile()