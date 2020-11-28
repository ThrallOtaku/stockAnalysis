from jqdatasdk import *
import pandas as pd
from datetime import date

id='18518326872'
password='84559515A'
auth(id,password)

pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)




#标普期货数据 ESmain
today=date.today()

#查询标普期货指数
#code='ES'
# dfList=finance.run_query(query(finance.FUT_GLOBAL_DAILY).filter(finance.FUT_GLOBAL_DAILY.day==today,finance.FUT_GLOBAL_DAILY.code==code))
# print(dfList)

#查询黄金期货指数近十天的价格
code='GC'
query=query(finance.FUT_GLOBAL_DAILY).filter(finance.FUT_GLOBAL_DAILY.code==code).order_by(finance.FUT_GLOBAL_DAILY.day.desc()).limit(10)
df=finance.run_query(query)
print(df)



#查询美股指数标普500('INX')近十天的指数数据
# q=query(finance.GLOBAL_IDX_DAILY).filter(finance.GLOBAL_IDX_DAILY.code=='INX').order_by(finance.GLOBAL_IDX_DAILY.day.desc()).limit(10)
# df=finance.run_query(q)
# print(df)

