# -*- coding: utf-8 -*-
'此类负责加载配置文件和获取配置文件中的参数'
__author__ = 'ly'

import os
import configparser

class ConfigManegment(object):
    _searchStep = None
    _targetFolderPath = None

    def __init__(self):
        self.readConfigFile()

    def readConfigFile(self):
        conf = configparser.ConfigParser()
        conf.read(os.getcwd()+'\\cfg.ini')
        self._searchStep = conf.get('Serach Step', 'len')
        self._targetFolderPath = conf.get('Target Path', 'path')
        #print(self._searchStep)
        #print('path %s' % self._targetFolderPath)

    def getSearchStep(self):
        return self._searchStep

    def getTargetFolderPath(self):
        return self._targetFolderPath

if __name__ == '__main__':
    ConfigManegment().readConfigFile()