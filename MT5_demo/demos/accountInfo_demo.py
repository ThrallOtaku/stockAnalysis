import MetaTrader5 as mt5
import pandas as pd

# 显示有关MetaTrader 5程序包的数据
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# 建立与MetaTrader 5程序端的连接
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# 连接到指定密码和服务器的交易账户
authorized = mt5.login(5249132, password="84559515A",server="ICMarketsSC-MT5")
if authorized:
    account_info = mt5.account_info()
    print(account_info)
    if account_info != None:
        # display trading account data 'as is'
        print(account_info)
        # display trading account data in the form of a dictionary
        print("Show account_info()._asdict():")
        account_info_dict = mt5.account_info()._asdict()
        for prop in account_info_dict:
            print("  {}={}".format(prop, account_info_dict[prop]))
        print()

        # 将词典转换为DataFrame和print
        df = pd.DataFrame(list(account_info_dict.items()), columns=['property', 'value'])
        print("account_info() as dataframe:")
        print(df)


# 断开与MetaTrader 5程序端的连接
mt5.shutdown()