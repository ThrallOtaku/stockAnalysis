from jqdatasdk import *
import pandas as pd


id='18518326872'
password='84559515A'
auth(id,password)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# from jqdatasdk import *
# #获取聚宽因子库所有因子
# df = get_all_factors()
# print(df)

#获取聚宽因子库营业收入TTM因子“operating_revenue_ttm”的分层回测收益
result=get_factor_effect('000300.XSHG','2016-07-29','2020-03-20','4W','size',5)
print(result)
