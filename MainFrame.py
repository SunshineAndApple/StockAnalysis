# -*- coding: utf-8 -*-
'此类是启动和初始化类，控制着开始'
__author_ = 'ly'

#sys
import sys
#mine
import AnalysisOneStock
class MainFrame(object):
    def main(self):
        a = AnalysisOneStock.AnalysisOneFile(sys.path[0], 'SH#600000.txt')
        a.readDataFromFile()
if __name__ == '__main__':
    MainFrame().main()
