# -*- coding: utf-8 -*-
'此类是启动和初始化类，控制着开始'
__author_ = 'ly'

#sys
import sys
import AnalysisOneStock
import ConfigManegment

class MainFrame(object):
    def main(self):
        #加载配置文件
        ConfigManegment.ConfigManegment()

        #开始分析
        a = AnalysisOneStock.AnalysisOneFile(sys.path[0], 'SH#601877.txt')
        a.readDataFromFile()
if __name__ == '__main__':
    MainFrame().main()
