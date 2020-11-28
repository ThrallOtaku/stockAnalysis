import MetaTrader5 as mt5

# 显示有关MetaTrader 5程序包的数据
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# 建立与MetaTrader 5程序端的连接
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# 尝试在市场报价中启用显示EURJPY交易品种
selected = mt5.symbol_select("EURJPY", True)
if not selected:
    print("Failed to select EURJPY")
    mt5.shutdown()
    quit()

# 显示EURJPY交易品种属性
symbol_info = mt5.symbol_info("EURJPY")
if symbol_info != None:
    # display the terminal data 'as is'
    print(symbol_info)
    print("EURJPY: spread =", symbol_info.spread, "  digits =", symbol_info.digits)
    # display symbol properties as a list
    print("Show symbol_info(\"EURJPY\")._asdict():")
    symbol_info_dict = mt5.symbol_info("EURJPY")._asdict()
    for prop in symbol_info_dict:
        print("  {}={}".format(prop, symbol_info_dict[prop]))

# 断开与MetaTrader 5程序端的连接
mt5.shutdown()