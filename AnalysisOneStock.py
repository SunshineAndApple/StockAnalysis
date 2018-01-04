# -*- coding: utf-8 -*-
'此类每次分析一个文件中的数据'
__author_ = 'ly'

#import MyLog
import Common
import SettlementAnaylsisByValue

class AnalysisOneFile(object):
    _fullPath = None      #文件全路径
    _fileName = None      #文件名称
    _InfoListAll = []     #一支股票原始的数据，行为分割

    _stockName = None     #股票名称
    _stockId = None       #股票ID


    def __init__(self, fullPath, fileName):
        if len(fullPath) == 0:
            raise ValueError('ERROR: file path empty!')

        self._fullPath = fullPath
        self._fileName = fileName



    def readDataFromFile(self):
        #myLogInfo = MyLog.MyLog().getLoggerByName('a')
        #myLogInfo.error('This is a error')
        filePath = self._fullPath + '\\' + self._fileName
        print('read file: ' + filePath)
        #read
        try:
            with open(filePath, 'r') as f:
                for line in f.readlines():
                    self._InfoListAll.append(line.strip())
            #删除最后一行的无效数据
            del self._InfoListAll[len(self._InfoListAll)-1]
            #获取股票信息，输出时候使用
            self.getStockNameAndId()
            #分析当前数据是否满足条件
            #   去除头两行，保留纯数据
            self._InfoListAll = self._InfoListAll[2:]
            settlementAnaylsisByValue = SettlementAnaylsisByValue.SettlementAnalysisByValue(self._InfoListAll)
            settlementAnaylsisByValue.analysisData()

        except Exception as e:
            raise

    def getStockNameAndId(self):
        firstLine = self._InfoListAll[0]
        temp = firstLine.split(' ')
        self._stockId = temp[Common.TitleIndex.STOCK_ID.value]
        self._stockName = temp[Common.TitleIndex.STOCK_NAME.value]


if __name__ == '__main__':
    pass
    #AnalysisOneStock('a', 'a').readDataFromFile()
