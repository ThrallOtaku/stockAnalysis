import MetaTrader5 as mt5
import pandas as pd

# 显示有关MetaTrader 5程序包的数据
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)
print()
# 建立与MetaTrader 5程序端的连接
if not mt5.initialize(login=25115284, server="MetaQuotes-Demo", password="4zatlbqx"):
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# 尝试在市场报价中启用显示EURCAD
selected = mt5.symbol_select("EURCAD", True)
if not selected:
    print("Failed to select EURCAD, error code =", mt5.last_error())
# 其他：
# symbol_info = mt5.symbol_info("EURCAD")
# print(symbol_info)
# print("EURCAD: currency_base =", symbol_info.currency_base, "  currency_profit =", symbol_info.currency_profit,
#       "  currency_margin =", symbol_info.currency_margin)
# print()
#
# # get symbol properties in the form of a dictionary
# print("Show symbol_info()._asdict():")
# symbol_info_dict = symbol_info._asdict()
# for prop in symbol_info_dict:
#     print("  {}={}".format(prop, symbol_info_dict[prop]))
# print()
#
# # 将词典转换为DataFrame和print
# df = pd.DataFrame(list(symbol_info_dict.items()), columns=['property', 'value'])
# print("symbol_info_dict() as dataframe:")
# print(df)
#
# # 断开与MetaTrader 5程序端的连接
# mt5.shutdown()