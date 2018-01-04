# -*- coding: utf-8 -*-
'此类以收盘价的方式来分析是否满足'
__author_ = 'ly'

import Common

class SettlementAnalysisByValue(object):
    #输入数据，未拆分。列格式为"日期,开盘,最高,最低,收盘,成交量,成交额
    _dataListAll = []
    #拆分后的数据值,只取_dataListAll中收盘一列，因为_dataListAll和_dataList的总数量
    #保持一致，所以迭代中如果需要其他数据，可以用_dataList的索引到_dataListAll中取
    _dataList = []


    def __init__(self, dataList=None):
        if dataList is None:
            dataList = []
        self._dataListAll = dataList

    #拆分数据，获取到每一天的收盘价
    def splitDataList(self):
        for var in self._dataListAll:
            tempList = var.split(',')
            self._dataList.append(tempList[Common.DataIndex.FINAL_PRICE.value])

    #
    #                                           b2
    #                                                         b3<=b2
    #                                                                     a4
    #                        b1=b2+(5%)b2 || b2-(5%)b2
    #                                                 a3<=a4
    #               a1?
    #                                a2

    # 解析数据
    def analysisData(self):
        self.splitDataList()
        print('当前数据有：%d行' % len(self._dataList))
        #print(self._dataList[0])
        #print(minP = min(self._dataList))

        #初始化职责链对象
        b2 = B2('B2')
        b1 = B2('B1')
        a3 = B2('A3')
        b3 = B2('B3')
        a4 = A4('A4')
        #设定执行顺序
        b2.setSuccessor(b1)
        b1.setSuccessor(a3)
        a3.setSuccessor(b3)
        b3.setSuccessor(a4)
        #初始条件
        request = Request()
        request.isAnalysis = False
        request.level = 'B2'
        request.resultList[0] = min(self._dataList)
        #执行分析
        b2.handleReuqest(request)
        zero = 1
        for var in request.resultList:
            zero = zero | var
            if 0 != (var | 0):
                print('第几个变量为符合： %s' % request.getVarNameFromList(request.resultList.index(var)))

        if 0 != zero:
            return True
        #不满足
        return False

#定义职责链
class Request(object):
    isAnalysis = False
    level = None
    # a2, b2, b1, a3, b3, a4序列为查找序列
    resultList = [0, 0, 0, 0, 0, 0]

    def getVarNameFromList(self, index):
        switcher = {0:'a2', 1:'b2', 2:'b1', 3:'a3', 4:'b3', 5:'a4'}


class Analysis(object):
    successor = None
    name = None

    def __init__(self, name):
        self.name = name

    def setSuccessor(self, successor):
        self.successor = successor

    def handleReuqest(self, request):
        pass

class B2(Analysis):
    def HandleReuqest(self, request):
        if request.isAnalysis == False and request.level == 'B2':
            print('b2')
            if self.successor != None:
                #下一级
                request.level = 'B1'
                request.isAnalysis = False
                self.successor.handleReuqest(request)

class B1(Analysis):
    def HandleReuqest(self, request):
        if request.isAnalysis == False and request.level == 'B1':
            print('b1')
            if self.successor != None:
                request.level = 'A3'
                request.isAnalysis = False
                self.successor.handleReuqest(request)

class A3(Analysis):
    def HandleReuqest(self, request):
        if request.isAnalysis == False and request.level == 'A3':
            print('a3')
            if self.successor != None:
                request.level = 'B3'
                request.isAnalysis = False
                self.successor.handleReuqest(request)

class B3(Analysis):
    def HandleReuqest(self, request):
        if request.isAnalysis == False and request.level == 'B3':
            print('b3')
            if self.successor != None:
                request.level = 'A4'
                request.isAnalysis = False
                self.successor.handleReuqest(request)

class A4(Analysis):
    def HandleReuqest(self, request):
        if request.isAnalysis == False and request.level == 'A4':
            print('a4')


