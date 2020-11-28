from datetime import datetime
import MetaTrader5 as mt5

# 显示有关MetaTrader 5程序包的数据
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# 建立与MetaTrader 5程序端的连接
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# 获取历史中的订单数量
from_date = datetime(2020, 1, 1)
to_date = datetime.now()
history_orders = mt5.history_orders_total(from_date, datetime.now())
if history_orders > 0:
    print("Total history orders=", history_orders)
# 其他：
# print("Orders not found in history")

# 断开与MetaTrader 5程序端的连接
mt5.shutdown()