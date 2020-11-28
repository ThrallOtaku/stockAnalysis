import MetaTrader5 as mt5

# 显示有关MetaTrader 5程序包的数据
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# 建立与MetaTrader 5程序端的连接
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# 检查是否存在活动订单
orders = mt5.orders_total()
if orders > 0:
    print("Total orders=", orders)

# 断开与MetaTrader 5程序端的连接
mt5.shutdown()