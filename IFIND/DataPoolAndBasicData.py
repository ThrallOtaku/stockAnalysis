from iFinDPy import *
#用户在使用时请修改成自己的账号和密码
thsLogin = THS_iFinDLogin("账号","密码")
if(thsLogin == 0 or thsLogin == -201):

	#利用数据池函数获取上证50在2016-11-27的成分股
    #数据池函数格式为THS_DataPool('modelName','inputParams','outputParams')
    #modelName不可以为空，且一次只能输入一个
    #inputParams用英文半角分号隔开，如inputParam1;inputParam2;inputParam3
    #outputParams用英文半角冒号赋值，用英文半角逗号分隔，Y表示该字段输出，N表示该字段不输出，如果不写则默认为Y,如outputParam1:Y,outputParam2:Y,outputParam3:N
    #THS_DataPool('modelName','inputParam1;inputParam2;inputParam3','outputParam1,outputParam2,outputParams3')
	#【001005260】是板块ID或者可以直接输入“上证50”，目前板块ID可以在【iFinD终端-工具-数据接口-板块ID查询工具】查看
    thsDataDataPool  = THS_DataPool('block','2016-11-27;001005260','date:Y,security_name:Y,thscode:Y')
    thsCodes = thsDataDataPool['tables'][0]['table']['THSCODE']
    f = open("DataPoolansBasicData.txt","a+")
    f.write("THSCode\t中文名称\t注册时间\t注册资金\n")
    for i in range(0,len(thsCodes)-1):
	
		#利用基础数据函数获取300033.SZ的首发上市日期
		#基础数据THS_BasicData('thsCodes','function','params');支持多证券单指标输入
		#thsCodes不可以为空，且支持多个输入，当有多个thsCodes则用英文半角逗号分隔，如thsCode1,thsCode2,thsCode3
		#function不可以为空，且当前只支持单个function，目前函数名称可以在【iFinD终端-工具-数据接口-指标函数查询工具】查看
		#params可以为空，也可以有多个，当有多个params时则用英文半角逗号分隔，如param1,param2,param3
		#THS_BasicData('thsCode1,thsCode2,thsCode3','function','param1,param2,param3')
        thsBasicData_gszwmc = THS_BasicData(thsCodes[i],"ths_corp_cn_name_stock","")
        stockname = thsBasicData_gszwmc['tables'][0]['table']['ths_corp_cn_name_stock'][0]
        thsBasicData_clrq = THS_BasicData(thsCodes[i],"ths_established_date_stock","")
        begintime = thsBasicData_clrq['tables'][0]['table']['ths_established_date_stock'][0]
        thsBasicData_zczb = THS_BasicData(thsCodes[i],"ths_reg_capital_stock","")
        registersaccount = thsBasicData_zczb['tables'][0]['table']['ths_reg_capital_stock'][0]
        f.write("%s\t%s\t%s\t%d\n"%(thsCodes[i], stockname, begintime,registersaccount))
    f.close()
else:
    print("登录失败")