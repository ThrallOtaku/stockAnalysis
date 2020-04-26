from iFinDPy import *
#用户在使用时请修改成自己的账号和密码
thsLogin = THS_iFinDLogin("账号","密码")
if(thsLogin == 0 or thsLogin == -201):
	
	#通过历史行情函数获取同花顺(300033.SZ)从2016-08-23到2016-11-23的开高低收数据
    #历史行情函数格式为THS_HistoryQuotes('thsCodes','indicators','params','startDate','endDate')
    #thsCodes不可以为空，且支持多个输入，当有多个thsCodes则用英文半角逗号分隔，如thsCode1,thsCode2,thsCode3
    #indicators不可以为空，且支持多个输入，当有多个indicators则用英文半角分号分隔，如indicator1;indicator2;indicator3
    #params不可以为空，且支持多个输入，当使用默认的参数时可以使用'default'表示，当用户只对其中某个指标设定而其他参数保持默认时，只需要输入设定的参数即可，如'period:W'
    #startDate的日期输入格式为YYYY-MM-DD
    #endDate的日期输入格式为YYYY-MM-DD
    #THS_HistoryQuotes('thsCode1,thsCode2,thsCode3','indicator1;indicator2;indicator3','param1,param2,param3','startDate','endDate')
    thsDataHistoryQuotes  = THS_HistoryQuotes("300033.SZ","open;high;low;close","period:D,pricetype:1,rptcategory:0,fqdate:1900-01-01,hb:YSHB","2016-03-01","2016-04-01")
    file = open("HistoryQuotes.txt","a+")
    file.write("THSCode\tTime\topen\thigh\tlow\tclose\n")
    thsCode = thsDataHistoryQuotes['tables'][0]['thscode']
    time = thsDataHistoryQuotes['tables'][0]['time']
    opens = thsDataHistoryQuotes['tables'][0]['table']['open']
    highs = thsDataHistoryQuotes['tables'][0]['table']['high']
    lows = thsDataHistoryQuotes['tables'][0]['table']['low']
    closes = thsDataHistoryQuotes['tables'][0]['table']['close']
    for i in range(0,len(time)-1):
        if(opens[i] == ''):
            opens[i] = float(opens[i])
        if(highs[i] == ''):
            highs[i] = float(highs[i])
        if(lows[i] == ''):
            lows[i] = float(lows[i])
        if(closes[i] == ''):
            closes[i] = float(closes[i])
        file.write("%s\t%s\t%f\t%f\t%f\t%f\n"%(thsCode,time[i],opens[i],highs[i],lows[i],closes[i]))
    file.close()
else:
    print("登录失败")
