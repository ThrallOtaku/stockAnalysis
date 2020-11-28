import csv
import pandas
import os

def doTransfer(file_name):
    tdx_file_name = "./TDX_FLODER/"+file_name+".txt"
    mt5_file_name = "./MT5_FLODER/"+file_name+".csv"
    date=[]
    open_price=[]
    high_price=[]
    low_price=[]
    close_price=[]
    tickvol=[]
    vol=[]
    spread=[]
    time=[]

    # with open 不用担心文件打开之后没有关闭，或者运行途中出错没有正确关闭占用系统资源的问题
    with open(tdx_file_name, 'r') as file:
        # 读取一行文件
        # first_line=file.readline()
        line_num = 0

        for line in file.readlines():
            line_num += 1
            #去掉表头前面三行,去掉尾部最后一行
            if (line_num > 4 and len(line)>60):
                single_line_list=line.split()
                date.append(single_line_list[0].replace("/","."))
                open_price.append(single_line_list[1])
                high_price.append(single_line_list[2])
                low_price.append(single_line_list[3])
                close_price.append(single_line_list[4])
                tickvol.append("100")
                vol.append("0")
                spread.append("0")
                time.append("15:00:00")
    # print(date)
    # print(open_price)
    # print(high_price)
    # print(low_price)
    # print(close_price)
    # print(tickvol)
    # print(vol)
    # print(spread)
    columnToData ={"<DATE>":date,"<TIME>":time,"<OPEN>":open_price,"<HIGH>":high_price,"<LOW>":low_price,
    "<CLOSE>":close_price,"<TICKVOL>":tickvol,"<VOL>":vol,"<SPREAD>":spread}
    #print(columnToData)
    data=pandas.DataFrame(columnToData)
    print(data)
    data.to_csv(mt5_file_name,index=False,encoding='utf-8')

#查询需要转换的文件夹
def scanDirs():
    from_dir="./TDX_FLODER/"
    to_dir="./MT5_FLODER/"
    fromfiles=[]
    tofiles=[]
    transferFiles = []
    #遍历来源文件夹
    for file in os.listdir(from_dir):
        #去掉后缀txt
        fromfiles.append(file.split(".")[0])

    for file in os.listdir(to_dir):
        tofiles.append(file.split(".")[0])
    print(fromfiles)
    print(tofiles)
    #如果tofiles 已经有了就不用转换了,如果tofiles里面没有的话就转换
    for name in fromfiles:
        if name not in tofiles:
            transferFiles.append(name)
    print(transferFiles)

    for file_name in transferFiles:
        doTransfer(file_name)


if __name__ == '__main__':
    scanDirs()
    #doTransfer()