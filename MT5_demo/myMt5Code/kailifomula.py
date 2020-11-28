#如果通信渠道的输入符号代表偶然事件的结果，在该偶然事件中，可以按照与其概率一致的赔率进行投注，
# 那么一个赌徒就可以利用输入符号给他的信息，使他的钱以指数形式增长

def kelly(p, q, rW, rL):
    """
    计算凯利公式
    Args:
        p (float): 获胜概率
        q (float): 失败概率
        rW (float): 净利润率
        rL (float): 净亏损率
    Returns:
        float: 最大化利润的投资本金占比(%)
    """
    return (p*rW - q*rL)/rW * rL

#手数:这里的结果是0.25，100美金的账户可以下25美金的损失。这样的保证金比例就到了400%
#为了预防不可控风险，我们将保证金比例控制在1000%以上。也就是说10美金以内。
#就相当于是下了10/25=0.4的凯利公式手数。10美金约等于0.03手黄金。单次下注的数量。如果低于这个回报太低。如果高了，风险太大。

#波动：黄金波动一个点。0.01手则是0.01美金。那么以下注为限的损失0.01手损失是3美金，300个点下行空间。就是3美金。

#点差:20-30,以最大为准，0.01手就是0.2-0.3美金

#在双向点差的情况下亏损3美金+0.6=3.6美金，需要盈利是7.2美金。才会形成指数级效应。

print(kelly(0.5,0.5,2,1))

#比如0.01 手黄金占预付款3 美金，那么凯利公式下面，我们假设下去的止损位置是3美金位置。如果更多的话，净亏损就会超过1.
#这样风险没法控制。那么盈利预期是6美金，如果高于这个可以追踪止盈。如果低于这个，没法获得长期的利润增长

