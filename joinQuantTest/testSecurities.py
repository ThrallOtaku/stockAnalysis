from jqdatasdk import *
import numpy as np
import pandas as pd


#解决数组打印不全的问题

id='18518326872'
password='84559515A'
auth(id,password)

pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)
#获取前两个证券
# securities=get_all_securities()[:2]
# print(securities)

#获取所有,股票个数，股票代码，stocks
# stocks = list(get_all_securities(['stock']).index)
# print(len(stocks),stocks)

#股票代码标准化
#normalize_code(['000001', 'SZ000001', '000001SZ', '000001.sz', '000001.XSHE'])


#获取平安银行2019-09-01至2019-09-22期间的集合竞价数据
# df=get_call_auction('000001.XSHE','2019-09-01','2019-09-22')
# print(df)

#龙虎榜数据
longhubang=get_billboard_list(None, None, '2020-3-17', 1)[:10]
print(longhubang)