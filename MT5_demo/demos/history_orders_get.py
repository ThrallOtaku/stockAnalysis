from datetime import datetime
import MetaTrader5 as mt5
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

# 获取历史中的订单数量
from_date = datetime(2020, 1, 1)
to_date = datetime.now()
history_orders = mt5.history_orders_get(from_date, to_date, group="*GBP*")
if history_orders == None:
    print("No history orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))
elif len(history_orders) > 0:
    print("history_orders_get({}, {}, group=\"*GBP*\")={}".format(from_date, to_date, len(history_orders)))
print()

# 根据持仓单号显示所有历史订单
position_id = 530218319
position_history_orders = mt5.history_orders_get(position=position_id)
if position_history_orders == None:
    print("No orders with position #{}".format(position_id))
    print("error code =", mt5.last_error())
elif len(position_history_orders) > 0:
    print("Total history orders on position #{}: {}".format(position_id, len(position_history_orders)))
    # 显示带有指定持仓单号的所有历史订单
    for position_order in position_history_orders:
        print(position_order)
    print()
    # display these orders as a table using pandas.DataFrame
    df = pd.DataFrame(list(position_history_orders), columns=position_history_orders[0]._asdict().keys())
    df.drop(
        ['time_expiration', 'type_time', 'state', 'position_by_id', 'reason', 'volume_current', 'price_stoplimit', 'sl',
         'tp'], axis=1, inplace=True)
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
    df['time_done'] = pd.to_datetime(df['time_done'], unit='s')
    print(df)

# 断开与MetaTrader 5程序端的连接
mt5.shutdown()