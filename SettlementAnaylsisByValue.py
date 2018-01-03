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

    #解析数据
    def analysisData(self):
        self.splitDataList()
        #print(len(self._dataList))
        #print(self._dataList[0])

    #拆分数据，获取到每一天的收盘价
    def splitDataList(self):
        for var in self._dataListAll:
            tempList = var.split(',')
            self._dataList.append(tempList[Common.DataIndex.FINAL_PRICE.value])
