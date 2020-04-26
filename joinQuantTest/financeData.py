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
# today=date.today()
# code='ES'
# dfList=finance.run_query(query(finance.FUT_GLOBAL_DAILY).filter(finance.FUT_GLOBAL_DAILY.day==today,finance.FUT_GLOBAL_DAILY.code==code))
# print(dfList)

#查询美股指数标普500('INX')近十天的指数数据
# q=query(finance.GLOBAL_IDX_DAILY).filter(finance.GLOBAL_IDX_DAILY.code=='INX').order_by(finance.GLOBAL_IDX_DAILY.day.desc()).limit(10)
# df=finance.run_query(q)
# print(df)


#大股东增减持
#指定查询对象为万科（000002.XSHE)的大股东增减持情况，返回条数为10条，2019-1-1以后的增减持情况，10条
# q2=query(finance.STK_SHAREHOLDERS_SHARE_CHANGE).filter(finance.STK_SHAREHOLDERS_SHARE_CHANGE.code=='000002.XSHE',
#                                                        finance.STK_SHAREHOLDERS_SHARE_CHANGE.pub_date>'2019-01-01').limit(10)
# d2=finance.run_query(q2)
# print(d2)


#查询华夏成长证券投资基金("000001")最近一个季度的基金持仓股票组合前10只股票，
fundList=['163402','163415','110003','161005','003095','000363','001410','110022','519712','162605','260108','162703',
          '000251','007802','166002','320022','001178','180031','007119','519700','001938']
for stock_code in fundList:
    print("stock_code is :" ,stock_code)
    # 查询华夏成长证券投资基金("000001")基金资产组合概况数据，传入的基金代码无需后缀
    q = query(finance.FUND_PORTFOLIO.code,
              finance.FUND_PORTFOLIO.name,
              finance.FUND_PORTFOLIO.pub_date,
              finance.FUND_PORTFOLIO.stock_rate,
              finance.FUND_PORTFOLIO.fixed_income_rate,
              finance.FUND_PORTFOLIO.total_asset).filter(finance.FUND_PORTFOLIO.code == stock_code).order_by(
        finance.FUND_PORTFOLIO.pub_date.desc()).limit(1)
    df = finance.run_query(q)

    print(df)
    #获取最近一个季度的前十持仓
    q3=query(finance.FUND_PORTFOLIO_STOCK).filter(finance.FUND_PORTFOLIO_STOCK.code==stock_code).order_by(finance.FUND_PORTFOLIO_STOCK.pub_date.desc()).limit(5)
    #返回数据类型dataframe
    df3=finance.run_query(q3)
    #取id=9630201的数据
    #print(df3[df3['id']==9630201])
    print(df3)




#查询所有股票按当日新增关注人数排名的前10只个股
# df4=finance.run_query(query(finance.STK_XUEQIU_PUBLIC).filter(finance.STK_XUEQIU_PUBLIC.day=='2018-12-04').order_by(finance.STK_XUEQIU_PUBLIC.new_follower.desc()).limit(10))
# print(df4)

#新闻联播文本数据
# df5=finance.run_query(query(finance.CCTV_NEWS).filter(finance.CCTV_NEWS.day=='2020-03-17').limit(10))
# print(df5)
# #进一步获取新闻正文内容
# print(df5.iloc[3,3])