from datetime import datetime
import MetaTrader5 as mt5

# 显示有关MetaTrader 5程序包的数据
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# 建立与MetaTrader 5程序端的连接
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# 获取历史中的交易数量
from_date = datetime(2020, 1, 1)
to_date = datetime.now()
deals = mt5.history_deals_total(from_date, to_date)
if deals > 0:
    print("Total deals=", deals)
# 其他：
# print("Deals not found in history")

# 断开与MetaTrader 5程序端的连接
mt5.shutdown()