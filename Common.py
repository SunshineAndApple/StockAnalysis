# -*- coding: utf-8 -*-
'此类中定义了通用的枚举值'

from enum import Enum, unique

#此类表示每一行数据位置，以逗号为间隔
@unique
class DataIndex(Enum):
    DATA = 1
    START_PRICE = 2
    MAX_PRICE = 3
    MIN_PRICE = 4
    FINAL_PRICE = 5 #收盘价
    TOTAL_COUNT = 6
    TOTAL_PRICE = 7

@unique
class TitleIndex(Enum):
    STOCK_ID = 0
    STOCK_NAME = 1

@unique
class ReaslutOfAnalysis(Enum):
    FALSE = 0
    TRUE = 1
