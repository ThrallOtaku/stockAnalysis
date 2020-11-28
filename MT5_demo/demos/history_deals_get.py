import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd

pd.set_option('display.max_columns', 500)  # number of columns to be displayed
pd.set_option('display.width', 1500)  # max table width to display
# 显示有关MetaTrader 5程序包的数据
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)
print()
# 建立与MetaTrader 5程序端的连接
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# 获取历史中的交易数量
from_date = datetime(2020, 1, 1)
to_date = datetime.now()
# 获取指定时间间隔内且名称包含"GBP"的交易品种的交易
deals = mt5.history_deals_get(from_date, to_date, group="*GBP*")
if deals == None:
    print("No deals with group=\"*USD*\", error code={}".format(mt5.last_error()))
elif len(deals) > 0:
    print("history_deals_get({}, {}, group=\"*GBP*\")={}".format(from_date, to_date, len(deals)))

# 获取名称中既不包含"EUR"也不包含"GBP"的交易品种的交易
deals = mt5.history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*")
if deals == None:
    print("No deals, error code={}".format(mt5.last_error()))
elif len(deals) > 0:
    print("history_deals_get(from_date, to_date, group=\"*,!*EUR*,!*GBP*\") =", len(deals))
    # display all obtained deals 'as is'
    for deal in deals:
        print("  ", deal)
    print()
    # display these deals as a table using pandas.DataFrame
    df = pd.DataFrame(list(deals), columns=deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df)
print("")

# 获取#530218319持仓相关的所有交易
position_id = 530218319
position_deals = mt5.history_deals_get(position=position_id)
if position_deals == None:
    print("No deals with position #{}".format(position_id))
    print("error code =", mt5.last_error())
elif len(position_deals) > 0:
    print("Deals with position id #{}: {}".format(position_id, len(position_deals)))
    # display these deals as a table using pandas.DataFrame
    df = pd.DataFrame(list(position_deals), columns=position_deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df)

# 断开与MetaTrader 5程序端的连接
mt5.shutdown()