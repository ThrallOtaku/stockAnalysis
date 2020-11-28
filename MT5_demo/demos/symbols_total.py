import MetaTrader5 as mt5

# 显示有关MetaTrader 5程序包的数据
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# 建立与MetaTrader 5程序端的连接
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# 获取交易品种的数量
symbols = mt5.symbols_total()
if symbols > 0:
    print("Total symbols =", symbols)


# 断开与MetaTrader 5程序端的连接
mt5.shutdown()