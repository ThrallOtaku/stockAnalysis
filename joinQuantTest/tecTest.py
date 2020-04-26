from jqdatasdk import *
import pandas as pd
#付费因子
# from jqlib.technical_analysis import *

id='18518326872'
password='84559515A'
auth(id,password)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# 定义股票池列表
security_list1 = '000001.XSHE'
security_list2 = ['000001.XSHE','000002.XSHE','601211.XSHG','603177.XSHG']

# 计算并输出 security_list1 的 CYF 值，
# CYF1 = CYF(security_list1, check_date='2017-01-04', N = 21)
# print CYF1[security_list1]
#
# # 输出 security_list2 的 CYF 值，付费因子
# CYF2 = CYF(security_list2, check_date='2017-01-04', N = 21)
# for stock in security_list2:
#     print CYF2[stock]