from iFinDPy import *
#用户在使用时请修改成自己的账号和密码
thsLogin = THS_iFinDLogin('账号','密码')

if(thsLogin == 0 or thsLogin == -201):
    
    #高频序列函数格式为THS_HighFrequenceSequence('thsCodes','indicators','params','startTime','endTime')
    #thsCodes不可以为空，且支持多个输入，当有多个thsCodes则用英文半角逗号分隔，如thsCode1,thsCode2,thsCode3
    #indicators不可以为空，且支持多个输入，当有多个indicators则用英文半角分号分隔，如indicator1;indicator2;indicator3
    #params不可以为空，且支持多个输入，当使用默认的参数时可以使用'default'表示，当用户只对其中某个指标设定而其他参数保持默认时，只需要输入设定的参数即可，如'Interval:5'
    #startDate的日期输入格式为YYYY-MM-DD HH:MM:SS
    #endDate的日期输入格式为YYYY-MM-DD HH:MM:SS
    #THS_HighFrequenceSequence('thsCode1,thsCode2,thsCode3','indicator1;indicator2;indicator3','param1,param2,param3','startTime','endTime')
    thsDataHighFrequenceSequence=THS_HighFrequenceSequence('600000.SH','open;high;low;close','CPS:no,baseDate:1900-01-01,MaxPoints:50000,Fill:Previous,Interval:1','2019-12-09 09:15:00','2019-12-09 15:15:00')
	highFrequenceSequence = THS_Trans2DataFrame(thsDataHighFrequenceSequence)
    
    #历史行情函数格式为THS_HistoryQuotes('thsCodes','indicators','params','startDate','endDate')
    #thsCodes不可以为空，且支持多个输入，当有多个thsCodes则用英文半角逗号分隔，如thsCode1,thsCode2,thsCode3
    #indicators不可以为空，且支持多个输入，当有多个indicators则用英文半角分号分隔，如indicator1;indicator2;indicator3
    #params不可以为空，且支持多个输入，当使用默认的参数时可以使用'default'表示，当用户只对其中某个指标设定而其他参数保持默认时，只需要输入设定的参数即可，如'period:W'
    #startDate的日期输入格式为YYYY-MM-DD
    #endDate的日期输入格式为YYYY-MM-DD
    #THS_HistoryQuotes('thsCode1,thsCode2,thsCode3','indicator1;indicator2;indicator3','param1,param2,param3','startDate','endDate')
    thsDataHistoryQuotes = THS_HistoryQuotes('300033.SZ','open;high;low;close','period:D,pricetype:1,rptcategory:0,fqdate:1900-01-01,hb:YSHB','2018-03-01','2018-04-01')
	historyQuotes = THS_Trans2DataFrame(thsDataHistoryQuotes)

    #实时行情函数的格式为THS_RealtimeQuotes('thsCodes','indicators','params')
    #thsCodes不可以为空，且支持多个输入，当有多个thsCodes则用英文半角逗号分隔，如thsCode1,thsCode2,thsCode3
    #indicators不可以为空，且支持多个输入，当有多个indicators则用英文半角分号分隔，如indicator1;indicator2;indicator3
    #params可以为空
    #THS_RealtimeQuotes('thsCode1,thsCode2,thsCode3','indicator1;indicator2;indicator3')
    thsDataRealtimeQuotes = THS_RealtimeQuotes('600000.SH,300033.SZ','open;high;low;new')
	realtimeQuotes = THS_Trans2DataFrame(thsDataRealtimeQuotes)
    
    #基础数据THS_BasicData('thsCodes','function','params');支持多证券单指标输入
    #thsCodes不可以为空，且支持多个输入，当有多个thsCodes则用英文半角逗号分隔，如thsCode1,thsCode2,thsCode3
    #function不可以为空，且当前只支持单个function，目前函数名称可以在【iFinD终端-工具-数据接口-指标函数查询工具】查看
    #params可以为空，也可以有多个，当有多个params时则用英文半角逗号分隔，如param1,param2,param3
    #THS_BasicData('thsCode1,thsCode2,thsCode3','function','param1,param2,param3')
    thsDataBasicData = THS_BasicData('600000.SH,600004.SH','ths_stock_short_name_stock;ths_ipo_date_stock',';')
	basicData = THS_Trans2DataFrame(thsDataBasicData)
    
    #日期系列函数格式为THS_DateSequence('thsCodes','indicators','params','startDate','endDate')
    #thsCodes不可以为空，且支持多个输入，当有多个thsCodes则用英文半角逗号分隔，如thsCode1,thsCode2,thsCode3
    #indicators不可以为空，且支持多个输入，当有多个indicators则用英文半角分号分隔，如indicator1;indicator2;indicator3
    #params不可以为空，且支持多个输入，当使用默认的参数时可以使用'default'表示，当用户只对其中某个指标设定而其他参数保持默认时，只需要输入设定的参数即可，如'Interval:M'
    #startDate的日期输入格式为YYYY-MM-DD
    #endDate的日期输入格式为YYYY-MM-DD
    #日期序列函数格式为THS_DateSerial('thsCode1,thsCode2,thsCode3','indicator1;indicator2;indicator3','param1,param2,param3','startDate','endDate')    
    thsDataDateSerial = THS_DateSerial('600000.SH,600004.SH','ths_total_shares_stock;ths_total_ashare_stock;ths_float_ashare_stock',';;','Days:Tradedays,Fill:Previous,Interval:D','2018-05-13','2018-06-13')
	dateSerial = THS_Trans2DataFrame(thsDataDateSerial)
    
    #数据池函数格式为THS_DataPool('modelName','inputParams','outputParams')
    #modelName不可以为空，且一次只能输入一个
    #inputParams用英文半角分号隔开，如inputParam1;inputParam2;inputParam3
    #outputParams用英文半角冒号赋值，用英文半角逗号分隔，Y表示该字段输出，N表示该字段不输出，如果不写则默认为Y,如outputParam1:Y,outputParam2:Y,outputParam3:N
    #THS_DataPool('modelName','inputParam1;inputParam2;inputParam3','outputParam1,outputParam2,outputParams3')
    #【001005260】是板块ID，目前板块ID可以在【iFinD终端-工具-数据接口-板块ID查询工具】查看
    thsDataDataPool = THS_DataPool('block','2016-12-19;001005260','date:Y,security_name:Y,thscode:Y')
	dataPool = THS_Trans2DataFrame(thsDataDataPool)
    
    #EDB数据请求函数格式为THS_EDBQuery('indicatorIDs','startDate','endDate')
    #indicatorIDs不可以为空，支持多个ID输入。指标ID可以在【iFinD终端-工具-数据接口】中的指标ID查询工具查看
    #startDate的日期输入格式为YYYY-MM-DD
    #endDate的日期输入格式为YYYY-MM-DD
    thsEDBDataQuery = THS_EDBQuery('M001620326;M002822183','2017-06-13','2018-06-13')
	edbDataQuery = THS_Trans2DataFrame(thsEDBDataQuery)
	
    #日内快照函数格式为THS_Snapshot('thsCodes','indicators','params','startTime','endTime')
    #thsCodes不可以为空，且支持多个输入，当有多个thsCodes则用英文半角逗号分隔，如thsCode1,thsCode2,thsCode3
    #indicators不可以为空，且支持多个输入，当有多个indicators则用英文半角分号分隔，如indicator1;indicator2;indicator3
    #params不可以为空，且当前只有一个参数，即dataType:Original
    #startDate的日期输入格式为YYYY-MM-DD HH:MM:SS
    #endDate的日期输入格式为YYYY-MM-DD HH:MM:SS
    #THS_Snapshot('thsCode1,thsCode2,thsCode3','indicator1;indicator2;indicator3','param1,param2,param3','startTime','endTime')
	thsDataSnapShot = THS_Snapshot('300033.SZ,600000.SH','tradeDate;tradeTime;preClose;open;high;low;latest','dataType:Original','2018-06-13 09:30:00','2018-06-13 09:45:00')
	snapShot = THS_Trans2DataFrame(thsDataSnapShot)
	
    #数据使用量查询函数，用于用户查询自身账号的数据使用量，其中行情数据是15000万条/周，基础数据是500万条/周，EDB数据是500条/周。通过高频序列函数、历史行情函数和实时行情函数获取的数据
    #统称为行情数据；通过基础数据函数、日期序列函数和数据池函数获取的数据统称为基础数据；通过EDB数据请求函数获取的数据统称为EDB数据。
    thsDataStatistics = THS_DataStatistics()
    
    #错误信息查询函数，对于函数执行后的errorcode进行查询，了解错误信息
    #value的值不可以为空，并且value的值必须是枚举出的错误值
    thsGetErrorInfo = THS_GetErrorInfo(0)
    
    #交易日期/日历日期查询函数
    #日期查询函数的格式是THS_DateQuery('exchange','dateType:value,period:value,dateFormat:value','startDate','endDate')
    #exchange不可以为空
    #dateType，period，dateFormat的值也不可以为空
    #startDate的日期输入格式为YYYY-MM-DD
    #endDate的日期输入格式为YYYY-MM-DD
    thsDateQuery = THS_DateQuery("SSE", "dateType:trade,period:D,dateFormat:0", "2016-07-21", "2016-08-21")
    
    #根据指定日期和偏移量找到相应的日期
    #日期偏移函数的格式是THS_DateQuery('exchange','dateType:value,period:value,dateFormat:value','date')
    #exchange不可以为空
    #dateType，period，dateFormat的值也不可以为空
    #date的日期输入格式为YYYY-MM-DD
    thsDateOffset = THS_DateOffset("SSE", "dateType:trade,period:W,offset:-10,dateFormat:0", "2016-08-21")
    
    #统计指定时间区间和日期类型中的日期数量
    #日期查询函数的格式是THS_DateCount('exchange','dateType:value,period:value,dateFormat:value','startDate','endDate')
    #exchange不可以为空
    #dateType，period，dateFormat的值也不可以为空
    #startDate的日期输入格式为YYYY-MM-DD
    #endDate的日期输入格式为YYYY-MM-DD
    thsDateCount = THS_DateCount("SSE", "dateType:trade,period:D,dateFormat:0", "2016-07-21", "2016-08-21")

	#登出函数
    thsLogout = THS_iFinDLogout()
else:
    print("登录失败")