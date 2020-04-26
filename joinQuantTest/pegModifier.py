# # 克隆自聚宽文章：https://www.joinquant.com/post/7433
# # 标题：对PEG策略进一步修改
# # 作者：nicklux
#
# import numpy as np
# import talib
# import pandas
# import scipy as sp
# import scipy.optimize
# import datetime as dt
# from scipy import linalg as sla
# from scipy import spatial
# from jqdata import gta
# from jqdata import *
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# import statsmodels.api as sm
#
# """
# 人家写的peg 策略。效果还可以。逻辑可以参考。代码跑不了。缺少包
# """
# def initialize(context):
#     set_benchmark('000300.XSHG')
#     set_slippage(FixedSlippage(0.000))
#     set_option('use_real_price', True)
#     log.set_level('order', 'error')
#     g.day_count = 0  # 调仓日计数器，单位：日
#     g.period = 5  # 调仓频率，单位：日
#     g.buy_stock_count = 5  # 买入股票最大数目
#     g.index2 = '000001.XSHG'
#     g.index8 = '399001.XSHE'
#     g.index_growth_rate = 0.01
#
#
# def handle_data(context, data):
#     # 没有大盘风控
#     if g.day_count % g.period == 0:
#         # print(g.day_count,g.period,(g.day_count % g.period))
#         log.info("==> 满足条件进行调仓")
#         buy_stocks = PEG_get_stock_list(context)
#         log.info("选股后可买股票: %s" % (buy_stocks))
#         adjust_position(context, buy_stocks)
#     g.day_count += 1
#     '''
#     #有大盘风控
#     # 回看指数前20天的涨幅
#     gr_index2 = get_growth_rate(g.index2)
#     gr_index8 = get_growth_rate(g.index8)
#     log.info("当前%s指数的20日涨幅 [%.2f%%]" %(get_security_info(g.index2).display_name, gr_index2*100))
#     log.info("当前%s指数的20日涨幅 [%.2f%%]" %(get_security_info(g.index8).display_name, gr_index8*100))
#
#     if gr_index2 <= g.index_growth_rate and gr_index8 <= g.index_growth_rate:
#         clear_position(context)
#         g.day_count = 0
#     else:
#         if g.day_count % g.period == 0:
#             log.info("==> 满足条件进行调仓")
#             buy_stocks = PEG_get_stock_list(context)
#             log.info("选股后可买股票: %s" %(buy_stocks))
#             adjust_position(context, buy_stocks)
#
#         else:
#             record(trade_type = 0)
#         g.day_count += 1
#     '''
#
#
# def adjust_position(context, buy_stocks):
#     for stock in list(context.portfolio.positions.keys()):
#         if stock not in buy_stocks:
#             log.info("stock [%s] in position is not buyable" % (stock))
#             position = context.portfolio.positions[stock]
#             close_position(position)
#         else:
#             log.info("stock [%s] is already in position" % (stock))
#
#     # 根据股票数量分仓
#     # 此处只根据可用金额平均分配购买，不能保证每个仓位平均分配
#     position_count = len(context.portfolio.positions)
#     if g.buy_stock_count > position_count:
#         value = context.portfolio.cash / (g.buy_stock_count - position_count)
#
#         for stock in buy_stocks:
#             if context.portfolio.positions[stock].total_amount == 0:
#                 if open_position(stock, value):
#                     if len(context.portfolio.positions) == g.buy_stock_count:
#                         break
#
#
# # 清空卖出所有持仓
# def clear_position(context):
#     if context.portfolio.positions:
#         log.info("==> 清仓，卖出所有股票")
#         for stock in list(context.portfolio.positions.keys()):
#             position = context.portfolio.positions[stock]
#             close_position(position)
#
#
# def close_position(position):
#     security = position.security
#     order = order_target_value_(security, 0)  # 可能会因停牌失败
#
#
# def open_position(security, value):
#     order = order_target_value_(security, value)
#     if order != None and order.filled > 0:
#         return True
#     return False
#
#
# def order_target_value_(security, value):
#     if value == 0:
#         log.debug("Selling out %s" % (security))
#     else:
#         log.debug("Order %s to value %f" % (security, value))
#     return order_target_value(security, value)
#
#
# def get_growth_rate(security, n=20):
#     lc = get_close_price(security, n)
#     # c = data[security].close
#     c = get_close_price(security, 1)
#     if not isnan(lc) and not isnan(c) and lc != 0:
#         return (c - lc) / lc
#     else:
#         log.error("数据非法, security: %s, %d日收盘价: %f, 当前价: %f" % (security, n, lc, c))
#         return 0
#
#
# def get_close_price(security, n, unit='1d'):
#     return attribute_history(security, n, unit, ('close'), True)['close'][0]
#
#
# # 根据PEG选取交易股票：原版的是用市值排序，修改版是用平均方差比排序
# def PEG_get_stock_list(context):
#     def fun_get_stock_market_cap(stock_list):
#         q = query(valuation.code, valuation.market_cap
#                   ).filter(valuation.code.in_(stock_list))
#         q2 = query(valuation.code, valuation.market_cap
#                    )
#         df = get_fundamentals(q).fillna(value=0)
#         df2 = get_fundamentals(q2).fillna(value=0).sort(columns='market_cap', ascending=True)
#         df2 = df2.reset_index(drop=True)
#         # print(df2)
#         sl = df.sort(columns='market_cap', ascending=True)['code'][:5]
#         for s in sl:
#             print((str(df2[df2.code == s].index.tolist()) + '/' + str(len(df2))))
#         tmpDict = df.to_dict()
#         stock_dict = {}
#         for i in range(len(list(tmpDict['code'].keys()))):
#             # 取得每个股票的 market_cap
#             stock_dict[tmpDict['code'][i]] = tmpDict['market_cap'][i]
#
#         return stock_dict
#
#     today = context.current_dt
#     # 获取当天市场所有的票
#     stock_list = list(get_all_securities(['stock'], today).index)
#     # 剔除上市不足120天，多日停牌，当日停牌，周期性行业的票
#     stock_list = fun_delNewShare(context, stock_list, 120)
#     stock_list = fun_del_pauses(stock_list)
#     stock_list = unpaused(stock_list)
#     stock_list = fun_remove_cycle_industry(stock_list)
#     # 获取剩下的票的增长数据：
#     # 过去4个季度的平均增长，最后1个季度的增长，增长标准差
#     stock_dict = fun_get_inc(context, stock_list)
#
#     old_stocks_list = []
#     for stock in list(context.portfolio.positions.keys()):
#         if stock in stock_list:
#             old_stocks_list.append(stock)
#
#     # 获取每只票的PEG
#     stock_list, buydict, as_dict = fun_cal_stock_PEG(context, stock_list, stock_dict)
#
#     # 根据市值升序排序
#     cap_dict = fun_get_stock_market_cap(stock_list)
#     buydict = sorted(list(cap_dict.items()), key=lambda d: d[1], reverse=False)
#     # 根据增长率的平均方差比降序排序
#     # buydict = sorted(as_dict.items(), key=lambda d:d[1], reverse=True)
#     if len(stock_list) < 5:
#         print(('可买数量只有：' + str(len(stock_list))))
#     buylist = []
#     i = 0
#     for idx in buydict:
#         if i < g.buy_stock_count:
#             stock = idx[0]
#             buylist.append(stock)  # 候选 stocks
#             # print (stock + ", PEG = "+ str(stock_PEG[stock]))
#             i += 1
#
#     # print (str(len(stock_list)) + " / " + str(len(buylist)))
#     print(buylist)
#     return buylist
#
#
# # 剔除上市时间较短的产品
# def fun_delNewShare(context, equity, deltaday):
#     deltaDate = context.current_dt.date() - dt.timedelta(deltaday)
#     tmpList = []
#     for stock in equity:
#         if get_security_info(stock).start_date < deltaDate:
#             tmpList.append(stock)
#     return tmpList
#
#
# # 剔除过去180天停牌时间超过1/3的股票
# def fun_del_pauses(_stock_list):
#     stock_list = []
#     for stock in _stock_list:
#         pau = attribute_history(stock, 180, unit='1d', fields=['paused'], \
#                                 skip_paused=False, df=True, fq='pre')
#         pau_days = len(pau[pau.paused == 1])
#         if pau_days / len(pau) < 0.3:
#             stock_list.append(stock)
#     return stock_list
#
#
# def unpaused(_stocklist):
#     current_data = get_current_data()
#     return [s for s in _stocklist if not current_data[s].paused]
#
#
# def fun_remove_cycle_industry(stock_list):
#     cycle_industry = [  # 'A01', #	农业 	1993-09-17
#         # 'A02', # 林业 	1996-12-06
#         # 'A03', #	畜牧业 	1997-06-11
#         # 'A04', #	渔业 	1993-05-07
#         # 'A05', #	农、林、牧、渔服务业 	1997-05-30
#         'B06',  # 煤炭开采和洗选业 	1994-01-06
#         'B07',  # 石油和天然气开采业 	1996-06-28
#         'B08',  # 黑色金属矿采选业 	1997-07-08
#         'B09',  # 有色金属矿采选业 	1996-03-20
#         'B11',  # 开采辅助活动 	2002-02-05
#         # 'C13', #	农副食品加工业 	1993-12-15
#         # C14 	食品制造业 	1994-08-18
#         # C15 	酒、饮料和精制茶制造业 	1992-10-12
#         # C17 	纺织业 	1992-06-16
#         # C18 	纺织服装、服饰业 	1993-12-31
#         # C19 	皮革、毛皮、羽毛及其制品和制鞋业 	1994-04-04
#         # C20 	木材加工及木、竹、藤、棕、草制品业 	2005-05-10
#         # C21 	家具制造业 	1996-04-25
#         # C22 	造纸及纸制品业 	1993-03-12
#         # C23 	印刷和记录媒介复制业 	1994-02-24
#         # C24 	文教、工美、体育和娱乐用品制造业 	2007-01-10
#         'C25',  # 石油加工、炼焦及核燃料加工业 	1993-10-25
#         'C26',  # 化学原料及化学制品制造业 	1990-12-19
#         # C27 	医药制造业 	1993-06-29
#         'C28',  # 化学纤维制造业 	1993-07-28
#         'C29',  # 橡胶和塑料制品业 	1992-08-28
#         'C30',  # 非金属矿物制品业 	1992-02-28
#         'C31',  # 黑色金属冶炼及压延加工业 	1994-01-06
#         'C32',  # 有色金属冶炼和压延加工业 	1996-02-15
#         'C33',  # 金属制品业 	1993-11-30
#         'C34',  # 通用设备制造业 	1992-03-27
#         'C35',  # 专用设备制造业 	1992-07-01
#         'C36',  # 汽车制造业 	1992-07-24
#         'C37',  # 铁路、船舶、航空航天和其它运输设备制造业 	1992-03-31
#         'C38',  # 电气机械及器材制造业 	1990-12-19
#         # C39 	计算机、通信和其他电子设备制造业 	1990-12-19
#         # C40 	仪器仪表制造业 	1993-09-17
#         'C41',  # 其他制造业 	1992-08-14
#         # C42 	废弃资源综合利用业 	2012-10-26
#         'D44',  # 电力、热力生产和供应业 	1993-04-16
#         # D45 	燃气生产和供应业 	2000-12-11
#         # D46 	水的生产和供应业 	1994-02-24
#         'E47',  # 房屋建筑业 	1993-04-29
#         'E48',  # 土木工程建筑业 	1994-01-28
#         'E50',  # 建筑装饰和其他建筑业 	1997-05-22
#         # F51 	批发业 	1992-05-06
#         # F52 	零售业 	1992-09-02
#         'G53',  # 铁路运输业 	1998-05-11
#         'G54',  # 道路运输业 	1991-01-14
#         'G55',  # 水上运输业 	1993-11-19
#         'G56',  # 航空运输业 	1997-11-05
#         'G58',  # 装卸搬运和运输代理业 	1993-05-05
#         # G59 	仓储业 	1996-06-14
#         # H61 	住宿业 	1993-11-18
#         # H62 	餐饮业 	1997-04-30
#         # I63 	电信、广播电视和卫星传输服务 	1992-12-02
#         # I64 	互联网和相关服务 	1992-05-07
#         # I65 	软件和信息技术服务业 	1992-08-20
#         'J66',  # 货币金融服务 	1991-04-03
#         'J67',  # 资本市场服务 	1994-01-10
#         'J68',  # 保险业 	2007-01-09
#         'J69',  # 其他金融业 	2012-10-26
#         'K70',  # 房地产业 	1992-01-13
#         # L71 	租赁业 	1997-01-30
#         # L72 	商务服务业 	1996-08-29
#         # M73 	研究和试验发展 	2012-10-26
#         'M74',  # 专业技术服务业 	2007-02-15
#         # N77 	生态保护和环境治理业 	2012-10-26
#         # N78 	公共设施管理业 	1992-08-07
#         # P82 	教育 	2012-10-26
#         # Q83 	卫生 	2007-02-05
#         # R85 	新闻和出版业 	1992-12-08
#         # R86 	广播、电视、电影和影视录音制作业 	1994-02-24
#         # R87 	文化艺术业 	2012-10-26
#         # S90 	综合 	1990-12-10
#     ]
#
#     for industry in cycle_industry:
#         stocks = get_industry_stocks(industry)
#         stock_list = list(set(stock_list).difference(set(stocks)))
#     return stock_list
#
#
# def fun_cal_stock_PEG(context, stock_list, stock_dict):
#     gr_index2 = get_growth_rate(g.index2)
#     gr_index8 = get_growth_rate(g.index8)
#     if not stock_list:
#         PEG = {}
#         avg_std = {}
#         return PEG, avg_std
#
#     q = query(valuation.code, valuation.pe_ratio
#               ).filter(valuation.code.in_(stock_list))
#
#     df = get_fundamentals(q).fillna(value=0)
#
#     tmpDict = df.to_dict()
#     pe_dict = {}
#     for i in range(len(list(tmpDict['code'].keys()))):
#         pe_dict[tmpDict['code'][i]] = tmpDict['pe_ratio'][i]
#     # print(pe_dict)
#     # 获取近两年有分红的票，以及他们的股息率
#     df = fun_get_Divid_by_year(context, stock_list)
#     if not len(df):
#         PEG = {}
#         avg_std = {}
#         return PEG, avg_std
#     # print(df)
#     tmpDict = df.to_dict()
#
#     stock_interest = {}
#     for stock in tmpDict['divpercent']:
#         stock_interest[stock] = tmpDict['divpercent'][stock]
#
#     h = history(1, '1d', 'close', stock_list, df=False)
#     PEG = {}
#     avg_std = {}
#     for stock in stock_list:
#         avg_inc = stock_dict[stock]['avg_inc']
#         last_inc = stock_dict[stock]['last_inc']
#         inc_std = stock_dict[stock]['inc_std']
#
#         pe = -1
#         if stock in pe_dict:
#             pe = pe_dict[stock]
#
#         interest = 0
#         if stock in stock_interest:
#             interest = stock_interest[stock]
#
#         PEG[stock] = -1
#         '''
#         原话大概是：
#         1、增长率 > 50 的公司要小心，高增长不可持续，一旦转差就要卖掉；实现的时候，直接卖掉增长率 > 50 个股票
#         2、增长平稳，不知道该怎么表达，用了 inc_std < last_inc。有思路的同学请告诉我
#         '''
#
#         if pe > 0 and last_inc <= 50 and last_inc > 0:  # and inc_std < last_inc:
#             PEG[stock] = (pe / (last_inc + interest * 100))
#             avg_std[stock] = avg_inc / inc_std
#     s_list = []
#     buydict = {}
#     as_dict = {}
#     for stock in list(PEG.keys()):
#         if PEG[stock] < 0.5 and PEG[stock] > 0:
#             s_list.append(stock)
#             buydict[stock] = PEG[stock]
#             as_dict[stock] = avg_std[stock]
#     if len(s_list) < g.buy_stock_count and (gr_index2 > g.index_growth_rate \
#                                             or gr_index8 > g.index_growth_rate):
#         print((str(len(s_list)) + '1次+'))
#         for stock in list(PEG.keys()):
#             if stock not in s_list:
#                 if PEG[stock] < 0.6 and PEG[stock] > 0:
#                     s_list.append(stock)
#                     buydict[stock] = PEG[stock]
#                     as_dict[stock] = avg_std[stock]
#     if len(s_list) < g.buy_stock_count and gr_index2 > (gr_index2 > g.index_growth_rate \
#                                                         or gr_index8 > g.index_growth_rate):
#         print((str(len(s_list)) + '2次+'))
#         for stock in list(PEG.keys()):
#             if stock not in s_list:
#                 if PEG[stock] < 0.7 and PEG[stock] > 0:
#                     s_list.append(stock)
#                     buydict[stock] = PEG[stock]
#                     as_dict[stock] = avg_std[stock]
#     if len(s_list) < g.buy_stock_count and (gr_index2 > g.index_growth_rate \
#                                             or gr_index8 > g.index_growth_rate):
#         print((str(len(s_list)) + '3次+'))
#         for stock in list(PEG.keys()):
#             if stock not in s_list:
#                 if PEG[stock] < 0.8 and PEG[stock] > 0:
#                     s_list.append(stock)
#                     buydict[stock] = PEG[stock]
#                     as_dict[stock] = avg_std[stock]
#     if len(s_list) < g.buy_stock_count and (gr_index2 > g.index_growth_rate \
#                                             or gr_index8 > g.index_growth_rate):
#         print((str(len(s_list)) + '4次+'))
#         for stock in list(PEG.keys()):
#             if stock not in s_list:
#                 if PEG[stock] < 0.9 and PEG[stock] > 0:
#                     s_list.append(stock)
#                     buydict[stock] = PEG[stock]
#                     as_dict[stock] = avg_std[stock]
#     if len(s_list) < g.buy_stock_count and (gr_index2 > g.index_growth_rate \
#                                             or gr_index8 > g.index_growth_rate):
#         print((str(len(s_list)) + '5次+'))
#         for stock in list(PEG.keys()):
#             if stock not in s_list:
#                 if PEG[stock] < 1 and PEG[stock] > 0:
#                     s_list.append(stock)
#                     buydict[stock] = PEG[stock]
#                     as_dict[stock] = avg_std[stock]
#
#     return s_list, buydict, as_dict
#
#
# def fun_get_Divid_by_year(context, stocks):
#     # 按照派息日计算，计算过去 12个月的派息率(TTM)
#     statsDate = context.current_dt
#     start_date = statsDate - dt.timedelta(366)
#     statsDate = statsDate - dt.timedelta(1)
#     year = statsDate.year
#
#     # 将当前股票池转换为国泰安的6位股票池
#     stocks_symbol = []
#     for s in stocks:
#         stocks_symbol.append(s[0:6])
#
#     # 按派息日，查找过去12个月的分红记录
#     # 4 steps
#     # 0、查找当年有分红的（受派息日约束）；
#     df = gta.run_query(query(
#         gta.STK_DIVIDEND.SYMBOL,  # 股票代码
#         # gta.STK_DIVIDEND.PLANDIVIDENTBT,        # 股票分红预案
#         # gta.STK_DIVIDEND.DECLAREDATE,
#         gta.STK_DIVIDEND.DIVIDENTAT,
#         gta.STK_DIVIDEND.DISTRIBUTIONBASESHARES  # 分红时的股本基数
#     ).filter(
#         gta.STK_DIVIDEND.DECLAREDATE < statsDate,
#         gta.STK_DIVIDEND.PAYMENTDATE >= start_date,
#         gta.STK_DIVIDEND.DIVDENDYEAR == year,
#         gta.STK_DIVIDEND.TERMCODE != 'P2799'
#     )).fillna(value=0, method=None, axis=0)
#
#     df = df[df.SYMBOL.isin(stocks_symbol)]
#     # 由于从df中将股票池的股票挑选了出来，index也被打乱，所以要重新更新index
#     df = df.reset_index(drop=True)
#
#     # 1、查找上一年有年度分红的（受派息日约束）；
#     df1 = gta.run_query(query(
#         gta.STK_DIVIDEND.SYMBOL,  # 股票代码
#         # gta.STK_DIVIDEND.PLANDIVIDENTBT,        # 股票分红预案
#         # gta.STK_DIVIDEND.DECLAREDATE,
#         gta.STK_DIVIDEND.DIVIDENTAT,
#         gta.STK_DIVIDEND.DISTRIBUTIONBASESHARES  # 分红时的股本基数
#     ).filter(
#         gta.STK_DIVIDEND.DECLAREDATE < statsDate,
#         gta.STK_DIVIDEND.PAYMENTDATE >= start_date,
#         gta.STK_DIVIDEND.DIVDENDYEAR == (year - 1),
#         gta.STK_DIVIDEND.TERMCODE == 'P2702',  # 年度分红
#         gta.STK_DIVIDEND.TERMCODE != 'P2799'
#     )).fillna(value=0, method=None, axis=0)
#     df1 = df1[df1.SYMBOL.isin(stocks_symbol)]
#     df1 = df1.reset_index(drop=True)
#
#     # 2、查找上一年非年度分红的（受派息日约束）；
#     df2 = gta.run_query(query(
#         gta.STK_DIVIDEND.SYMBOL,  # 股票代码
#         # gta.STK_DIVIDEND.PLANDIVIDENTBT,        # 股票分红预案
#         # gta.STK_DIVIDEND.DECLAREDATE,
#         gta.STK_DIVIDEND.DIVIDENTAT,
#         gta.STK_DIVIDEND.DISTRIBUTIONBASESHARES  # 分红时的股本基数
#     ).filter(
#         gta.STK_DIVIDEND.DECLAREDATE < statsDate,
#         gta.STK_DIVIDEND.PAYMENTDATE >= start_date,
#         gta.STK_DIVIDEND.DIVDENDYEAR == (year - 1),
#         gta.STK_DIVIDEND.TERMCODE != 'P2702',  # 年度分红
#         gta.STK_DIVIDEND.TERMCODE != 'P2799'
#     )).fillna(value=0, method=None, axis=0)
#     df2 = df2[df2.SYMBOL.isin(stocks_symbol)]
#     df2 = df2.reset_index(drop=True)
#     # print(df2)
#     # 得到目前看起来，有上一年度年度分红的股票
#     stocks_symbol_this_year = list(set(list(df1['SYMBOL'])))
#     # 得到目前看起来，上一年度没有年度分红的股票
#     stocks_symbol_past_year = list(set(stocks_symbol) - set(stocks_symbol_this_year))
#
#     # 3、查找上一年度还没分红，但上上年有分红的（受派息日约束）
#     df3 = gta.run_query(query(
#         gta.STK_DIVIDEND.SYMBOL,  # 股票代码
#         # gta.STK_DIVIDEND.PLANDIVIDENTBT,        # 股票分红预案
#         gta.STK_DIVIDEND.DIVIDENTAT,
#         gta.STK_DIVIDEND.DISTRIBUTIONBASESHARES  # 分红时的股本基数
#     ).filter(
#         gta.STK_DIVIDEND.DECLAREDATE < statsDate,
#         gta.STK_DIVIDEND.PAYMENTDATE >= start_date,
#         gta.STK_DIVIDEND.DIVDENDYEAR == (year - 2),
#         # gta.STK_DIVIDEND.TERMCODE == 'P2702',   # 年度分红
#         gta.STK_DIVIDEND.TERMCODE != 'P2799'
#     )).fillna(value=0, method=None, axis=0)
#     df3 = df3[df3.SYMBOL.isin(stocks_symbol_past_year)]
#     df3 = df3.reset_index(drop=True)
#     # 3表合并
#     df = pd.concat((df, df1))
#     df = pd.concat((df, df2))
#     df = pd.concat((df, df3))
#     # 将股票代码转为聚宽适用格式
#     df['SYMBOL'] = list(map(normalize_code, list(df['SYMBOL'])))
#     df.index = list(df['SYMBOL'])
#
#     # 获取最新股本
#     q = query(valuation.code, valuation.capitalization)
#     df2 = get_fundamentals(q).fillna(value=0)
#
#     df2 = df2[df2.code.isin(df.index)]
#     df2['SYMBOL'] = df2['code']
#
#     df2 = df2.drop(['code'], axis=1)
#
#     # 合并成一个 dataframe
#     df = df.merge(df2, on='SYMBOL')
#     df.index = list(df['SYMBOL'])
#     df = df.drop(['SYMBOL'], axis=1)
#
#     # 转换成 float
#     df['DISTRIBUTIONBASESHARES'] = list(map(float, df['DISTRIBUTIONBASESHARES']))
#     # 计算股份比值
#     df['CAP_RATIO'] = df['DISTRIBUTIONBASESHARES'] / (df['capitalization'] * 10000)
#
#     df['DIVIDENTAT'] = list(map(float, df['DIVIDENTAT']))
#     # 计算相对于目前股份而言的分红额度
#     df['DIVIDENTAT'] = df['DIVIDENTAT'] * df['CAP_RATIO']
#
#     # df = df.drop(['PLANDIVIDENTBT', 'DISTRIBUTIONBASESHARES','capitalization','CAP_RATIO'], axis=1)
#     df = df.drop(['DISTRIBUTIONBASESHARES', 'capitalization', 'CAP_RATIO'], axis=1)
#     # print(df)
#     # 接下来这一步是考虑多次分红的股票，因此需要累加股票的多次分红
#     df = df.groupby(df.index).sum()
#     # print('df',df)
#     # print(df[df.index == '002695.XSHE'])
#     # 得到当前股价
#     if len(list(df.index)) != 0:
#         Price = history(1, unit='1d', field='close', security_list=list(df.index), df=True, skip_paused=False, fq='pre')
#         Price = Price.T
#         df['pre_close'] = Price
#         # print(df)
#         # 计算股息率 = 股息/股票价格，* 10 是因为取到的是每 10 股分红
#         df['divpercent'] = df['DIVIDENTAT'] / (df['pre_close'] * 10)
#         df = df.drop(['pre_close', 'DIVIDENTAT'], axis=1)
#         df = df[df.divpercent > 0]
#         return df
#     else:
#         return df
#
#
# # 取得净利润增长率参数
# def fun_get_inc(context, stock_list):
#     # 取最近的四个季度财报的日期
#     def __get_quarter(stock_list):
#         '''
#         输入 stock_list
#         返回最近 n 个财报的日期
#         返回每个股票最近一个财报的日期
#         '''
#         # 取最新一季度的统计日期
#         q = query(indicator.code, indicator.statDate
#                   ).filter(indicator.code.in_(stock_list))
#         df = get_fundamentals(q)
#
#         stock_last_statDate = {}
#         tmpDict = df.to_dict()
#         for i in range(len(list(tmpDict['statDate'].keys()))):
#             # 取得每个股票的代码，以及最新的财报发布日
#             stock_last_statDate[tmpDict['code'][i]] = tmpDict['statDate'][i]
#
#         df = df.sort(columns='statDate', ascending=False)
#         # 取得最新的财报日期
#         last_statDate = df.iloc[0, 1]
#
#         this_year = int(str(last_statDate)[0:4])
#         this_month = str(last_statDate)[5:7]
#
#         if this_month == '12':
#             last_quarter = str(this_year) + 'q4'
#             last_two_quarter = str(this_year) + 'q3'
#             last_three_quarter = str(this_year) + 'q2'
#             last_four_quarter = str(this_year) + 'q1'
#             last_five_quarter = str(this_year - 1) + 'q4'
#
#         elif this_month == '09':
#             last_quarter = str(this_year) + 'q3'
#             last_two_quarter = str(this_year) + 'q2'
#             last_three_quarter = str(this_year) + 'q1'
#             last_four_quarter = str(this_year - 1) + 'q4'
#             last_five_quarter = str(this_year - 1) + 'q3'
#
#         elif this_month == '06':
#             last_quarter = str(this_year) + 'q2'
#             last_two_quarter = str(this_year) + 'q1'
#             last_three_quarter = str(this_year - 1) + 'q4'
#             last_four_quarter = str(this_year - 1) + 'q3'
#             last_five_quarter = str(this_year - 1) + 'q2'
#
#         else:  # this_month == '03':
#             last_quarter = str(this_year) + 'q1'
#             last_two_quarter = str(this_year - 1) + 'q4'
#             last_three_quarter = str(this_year - 1) + 'q3'
#             last_four_quarter = str(this_year - 1) + 'q2'
#             last_five_quarter = str(this_year - 1) + 'q1'
#
#         return last_quarter, last_two_quarter, last_three_quarter, last_four_quarter, last_five_quarter, stock_last_statDate
#
#     # 查财报，返回指定值
#     def __get_fundamentals_value(stock_list, myDate):
#         '''
#         输入 stock_list, 查询日期
#         返回指定的财务数据，格式 dict
#         '''
#         q = query(indicator.code, indicator.inc_net_profit_year_on_year, indicator.statDate,
#                   indicator.inc_net_profit_to_shareholders_year_on_year).filter(indicator.code.in_(stock_list))
#
#         df = get_fundamentals(q, statDate=myDate).fillna(value=0)
#
#         tmpDict = df.to_dict()
#         stock_dict = {}
#         for i in range(len(list(tmpDict['statDate'].keys()))):
#             tmpList = []
#             tmpList.append(tmpDict['statDate'][i])
#             tmpList.append(tmpDict['inc_net_profit_to_shareholders_year_on_year'][i])
#             # 原版使用的是下面的‘净利润同比增长’，但是修改使用‘归属母公司净利润同比增长’收益更高
#             # tmpList.append(tmpDict['inc_net_profit_year_on_year'][i])
#             stock_dict[tmpDict['code'][i]] = tmpList
#
#         return stock_dict
#
#     # 对净利润增长率进行处理
#     def __cal_net_profit_inc(inc_list):
#
#         inc = inc_list
#
#         for i in range(len(inc)):  # 约束在 +- 100 之内，避免失真
#             if inc[i] > 100:
#                 inc[i] = 100
#             if inc[i] < -100:
#                 inc[i] = -100
#
#         avg_inc = np.mean(inc[:4])
#         last_inc = inc[0]
#         inc_std = np.std(inc)
#
#         return avg_inc, last_inc, inc_std
#
#     # 得到最近 n 个季度的统计时间
#     last_quarter, last_two_quarter, last_three_quarter, last_four_quarter, last_five_quarter, stock_last_statDate = __get_quarter(
#         stock_list)
#
#     last_quarter_dict = __get_fundamentals_value(stock_list, last_quarter)
#     # print(last_quarter_dict)
#     last_two_quarter_dict = __get_fundamentals_value(stock_list, last_two_quarter)
#     last_three_quarter_dict = __get_fundamentals_value(stock_list, last_three_quarter)
#     last_four_quarter_dict = __get_fundamentals_value(stock_list, last_four_quarter)
#     last_five_quarter_dict = __get_fundamentals_value(stock_list, last_five_quarter)
#
#     stock_dict = {}
#     for stock in stock_list:
#         inc_list = []
#
#         if stock in stock_last_statDate:
#             if stock in last_quarter_dict:
#                 if stock_last_statDate[stock] == last_quarter_dict[stock][0]:
#                     inc_list.append(last_quarter_dict[stock][1])
#
#             if stock in last_two_quarter_dict:
#                 inc_list.append(last_two_quarter_dict[stock][1])
#             else:
#                 inc_list.append(0)
#
#             if stock in last_three_quarter_dict:
#                 inc_list.append(last_three_quarter_dict[stock][1])
#             else:
#                 inc_list.append(0)
#
#             if stock in last_four_quarter_dict:
#                 inc_list.append(last_four_quarter_dict[stock][1])
#             else:
#                 inc_list.append(0)
#
#             if stock in last_five_quarter_dict:
#                 inc_list.append(last_five_quarter_dict[stock][1])
#             else:
#                 inc_list.append(0)
#         else:
#             inc_list = [0, 0, 0, 0]
#         # print(inc_list)
#         # 取得过去4个季度的平均增长，最后1个季度的增长，增长标准差
#         avg_inc, last_inc, inc_std = __cal_net_profit_inc(inc_list)
#         # print(stock,inc_std)
#         stock_dict[stock] = {}
#         stock_dict[stock]['avg_inc'] = avg_inc
#         stock_dict[stock]['last_inc'] = last_inc
#         stock_dict[stock]['inc_std'] = inc_std
#
#     return stock_dict
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
