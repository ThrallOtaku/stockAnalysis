import MetaTrader5 as mt5

# 显示有关MetaTrader 5程序包的数据
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# 建立与MetaTrader 5程序端的连接
if not mt5.initialize():
    print("initialize() failed")
    quit()

# 显示有关连接状态、服务器名称和交易账户的数据
print(mt5.terminal_info())
# 显示有关MetaTrader 5版本的数据
print(mt5.version())

# 断开与MetaTrader 5程序端的连接
mt5.shutdown()