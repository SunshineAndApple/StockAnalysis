# -*- coding: utf-8 -*-
'此类以收盘价的方式来分析是否满足'
__author_ = 'ly'

import Common
import ConfigManegment
import LogInfo
import ConfigManegment




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
            self._dataList.append(int(tempList[Common.DataIndex.FINAL_PRICE.value]))

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
        LogInfo.LogInfo().debugLog('当前数据有：%d行' % len(self._dataList))
        LogInfo.LogInfo().debugLog('当前最小值: %d' % min(self._dataList))

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
        request.valueList = self._dataList
        #print(request.valueList)
        #执行分析
        b2.handleReuqest(request)
        #获取结果
        zero = 1
        for var in request.resultList:
            zero = zero | int(var)
            if 0 != (int(var) | 0):
                #print(request.resultList)
                LogInfo.LogInfo().debugLog('节点%s有符合的值且值为： %s' % (request.getVarNameFromList(request.resultList.index(var)), var))

        if 0 != zero:
            return True
        #不满足
        return False

class ValueType(object):
    MAX_VALUE = 0
    MIN_VALUE = 1

class ResultListIndex(object):
    A2 = 0
    B2 = 1
    B1 = 2
    A3 = 3
    B3 = 4
    A4 = 5

#定义职责链
class Request(object):
    isAnalysis = False
    level = None
    # a2, b2, b1, a3, b3, a4序列为查找序列
    resultList = [0, 0, 0, 0, 0, 0]
    #valueList = SettlementAnalysisByValue._dataList
    valueList = None

    def getVarNameFromList(self, index):
        switcher = {0:'a2', 1:'b2', 2:'b1', 3:'a3', 4:'b3', 5:'a4'}
        return switcher.get(index)

    #type:取值类型：max min
    #sorStartIndex: 开始目标resultListIndex的索引
    #targetIndex: resultListIndex目标值的索引
    def getMaxOrMinValue(self, type, resultListIndex, targetIndex):
        if 0 != self.resultList[resultListIndex]:
            # 标准步长
            step = ConfigManegment.ConfigManegment().getSearchStep()
            print(type, resultListIndex, targetIndex)

            if (ResultListIndex.A2 == resultListIndex) and (ResultListIndex.B1 == targetIndex):
                # A2
                endIndex = self.valueList.index(self.request[resultListIndex])
                print('if : endIndex')
                if 0 <= ((endIndex - step * 2)):
                    startIndex = ndIndex - step * 2
                else:
                    startIndex = 0
            else:
                LogInfo.LogInfo().debugLog('else : startIndex')
                startIndex = self.valueList.index(self.resultList[resultListIndex])
                LogInfo.LogInfo().debugLog('startIndex: %d' % startIndex)
                if len(self.valueList) >= ((int(startIndex) + int(step) * 2)):
                    endIndex = (int(startIndex) + int(step) * 2)
                else:
                    endIndex = len(request.valueList)

            # 切片是[a, a)，所以这里需要加1
            if ValueType.MAX_VALUE == type:
                self.resultList[targetIndex] = max(self.valueList[startIndex:endIndex + 1])
            elif ValueType.MIN_VALUE == type:
                self.resultList[targetIndex] = min(self.valueList[startIndex:endIndex + 1])

        else:
            pass

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
    def handleReuqest(self, request):
        LogInfo.LogInfo().debugLog('开始分析b2')
        #b1 a2 b2
        request.getMaxOrMinValue(ValueType.MAX_VALUE, ResultListIndex.A2, ResultListIndex.B2)

        if self.successor != None:
            self.successor.handleReuqest(request)

class B1(Analysis):
    def handleReuqest(self, request):
        LogInfo.LogInfo().debugLog('开始分析b1')
        # b1 a2 b2
        request.getMaxOrMinValue(ValueType.MAX_VALUE, ResultListIndex.A2.value, ResultListIndex.B1.value)

        #  (b2-8%b2) < b1 < (b2+5%b2)
        if ((request.resultList[ResultListIndex.B1.value] <
             (request.resultList[ResultListIndex.B2.value]+request.resultList[ResultListIndex.B2.value]*0.5)) and
                (request.resultList[ResultListIndex.B1.value] > (request.resultList[ResultListIndex.B2.value] -
                                                                 request.resultList[ResultListIndex.B2.value] * 0.8))):
            pass
        else:
            request.resultList[ResultListIndex.B1.value] = 0

        if self.successor != None:
            self.successor.handleReuqest(request)

class A3(Analysis):
    def handleReuqest(self, request):
        LogInfo.LogInfo().debugLog('开始分析a3')
        #  a2 b2 a3
        request.getMaxOrMinValue(ValueType.MIN_VALUE, ResultListIndex.B2.value, ResultListIndex.A3.value)

        if self.successor != None:
            self.successor.handleReuqest(request)

class B3(Analysis):
    def HandleReuqest(self, request):
        LogInfo.LogInfo().debugLog('开始分析b3')
        #  b2 a3 b3
        request.getMaxOrMinValue(ValueType.MAX_VALUE, ResultListIndex.A3.value, ResultListIndex.B3.value)

        if (request.resultList[4] <= request.resultList[1]):
            pass
        else:
            request.resultList[4] = 0

        if self.successor != None:
            self.successor.handleReuqest(request)

class A4(Analysis):
    def handleReuqest(self, request):
        if self.successor != None:
            LogInfo.LogInfo().debugLog('开始分析a4')
            request.getMaxOrMinValue(ValueType.MIN_VALUE, ResultListIndex.B3.value, ResultListIndex.A4.value)

            if (request.resultList[ResultListIndex.A3.value] <= request.resultList[ResultListIndex.A4.value]):
                pass
            else:
                request.resultList[5] = 0


if __name__ == '__main__':
    pass