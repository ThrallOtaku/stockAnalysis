# -*- coding: utf-8 -*-
"""
Created on Fri Mar 02 10:40:33 2018

@author: Administrator
"""

from iFinDPy import *
#用户在使用时请修改成自己的账号和密码
thsLogin = THS_iFinDLogin('账号','密码')

if(thsLogin == 0 or thsLogin == -201):
    #股票-股票市场类-深证A股:001005030
    Code_list = THS_DataPool('block','2015-04-25;001005030','date:Y,thscode:Y,security_name:Y')
    thsData = THS_Trans2DataFrame(Code_list)
    codes=thsData.THSCODE
    codeList = ','.join(codes)
    # print(codes)
    # codes.to_csv('code.csv')
    indicators = 'ths_gpjc_stock;ths_gpdm_stock;ths_thsdm_stock'
    indicatorParams = ';;'
    params = 'Days:Tradedays,Fill:Previous,Interval:D'
    sd = '2018-01-27'
    ed = '2018-02-27'
    
    data = THS_DateSerial(codeList,indicators,indicatorParams,params,sd,ed)
    tData = THS_Trans2DataFrame(data)
    print(tData)
    
    
    thsLogout = THS_iFinDLogout()
else:
    print("登录失败")