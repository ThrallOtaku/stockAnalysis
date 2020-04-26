from jqdatasdk import *
import pandas as pd

id='18518326872'
password='84559515A'
auth(id,password)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_colwidth',1000)

# 查询分地区农林牧渔业总产值表(季度累计) 的前10条数据
# q = query(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_QUARTER
#     ).limit(10)
# df = macro.run_query(q)
# print(df)

#房价指数,打电话给聚宽，是不是不维护房价的宏观数据了
# q2 = query(macro.MAC_INDUSTRY_ESTATE_70CITY_INDEX_MONTH)
# df2= macro.run_query(q2)
# print(df2)
# print(df2[df2['stat_month']=='2020-12'])


# 获取因子Skewness60(个股收益的60日偏度)从 2017-01-01 至 2017-03-04 的因子值
# factor_data = get_factor_values(securities=['000001.XSHE'], factors=['Skewness60','DEGM','quick_ratio'], start_date='2017-01-01', end_date='2017-03-04')
# # 查看因子值
# print(factor_data['Skewness60'])
#
# print(get_all_factors())

