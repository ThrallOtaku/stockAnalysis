from selenium import webdriver
from _datetime import datetime
import common.xgb_data as xd
import common.sqlite_oper as so
import time, json

#################################################
dapan = []  # 大盘数据
lianbanlist = []  # 涨停数据列表


# ——————判断是否有当天数据——————
# 返回值为0表示没有date日期的数据
def isload(date):
    sql = "select * from dapan where downdate='" + str(date) + "'"
    result = so.select(sql)
    return len(result)


# ——————将数据保存到sqlite数据库——————
# 返回值为0表示没有date日期的数据
def save_to_sqlite():
    # 保存大盘数据
    sql = "insert into dapan values('{0}',{1},{2},{3},{4},'{5}',{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16});".format(
        dapan.downdate, dapan.up, dapan.down, dapan.limitUp, dapan.limitDown, dapan.bomb, dapan.ban1, dapan.ban2,
        dapan.ban3,
        dapan.ban4, dapan.ban5, dapan.ban6, dapan.ban7, dapan.ban8, dapan.ban9, dapan.ban10, dapan.ban10s)
    so.exec(sql)
    # 保存涨停股数据
    for zt in lianbanlist:
        sql = "insert into zhangting values('{0}','{1}','{2}','{3}','{4}',{5});".format(
            zt.downdate, zt.scode, zt.sname, zt.stype, zt.zttime, zt.slevel)
        so.exec(sql)
    print(dapan.downdate + "的数据保存完毕")


# ——————统计每种连板情况的个数——————
def calc_lianban_amount(i):
    if i == 1:
        dapan.ban1 = int(dapan.ban1) + 1
    elif i == 2:
        dapan.ban2 += 1
    elif i == 3:
        dapan.ban3 += 1
    elif i == 4:
        dapan.ban4 += 1
    elif i == 5:
        dapan.ban5 += 1
    elif i == 6:
        dapan.ban6 += 1
    elif i == 7:
        dapan.ban7 += 1
    elif i == 8:
        dapan.ban8 += 1
    elif i == 9:
        dapan.ban9 += 1
    elif i == 10:
        dapan.ban10 += 1
    else:
        dapan.ban10s += 1


# ————得到大盘数据————
# 获取当天数据不用加日期，历史数据必须加date=xxxx-xx-xx
def get_today_data(date=datetime.now().date()):
    try:
        if (isload(date) > 0):
            print("已经下载过" + str(date) + "的数据")
            return

        # ——创建大盘数据对象——
        global dapan  # 说明该变量是全局变量
        dapan = xd.DaPan(str(date), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        # browser = webdriver.Chrome()
        # ——大盘涨跌数量——
        url = "https://flash-api.xuangubao.cn/api/market_indicator/line?fields=rise_count,fall_count"
        if (date != datetime.now().date()):
            url += "&date=" + str(date)
        browser.get(url)
        page = str(browser.page_source)  # 得到大盘涨跌数据
        page = page[page.find("{"):-20]
        data = json.loads(page)["data"]
        if (len(data) <= 0):
            print("没有" + str(date) + "的数据")
            return
        d = json.loads(page)["data"][-1]  # 得到最后一次数据（收盘数据）
        dapan.up = d["rise_count"]  # 下跌数量
        dapan.down = d["fall_count"]  # 上涨数量

        time.sleep(1)
        # ——大盘涨跌停数量——
        url = "https://flash-api.xuangubao.cn/api/market_indicator/line?fields=limit_up_count,limit_down_count"
        if (date != datetime.now().date()):
            url += "&date=" + str(date)
        browser.get(url)
        page = str(browser.page_source)  # 得到页面源码
        page = page[page.find("{"):-20]
        d = json.loads(page)["data"][-1]  # 得到最后一次数据（收盘数据）
        dapan.limitUp = d["limit_up_count"]
        dapan.limitDown = d["limit_down_count"]

        time.sleep(1)
        # ——炸板率——
        url = "https://flash-api.xuangubao.cn/api/market_indicator/line?fields=limit_up_broken_count,limit_up_broken_ratio"
        if (date != datetime.now().date()):
            url += "&date=" + str(date)
        browser.get(url)
        page = str(browser.page_source)  # 得到页面源码
        page = page[page.find("{"):-20]
        d = json.loads(page)["data"][-1]  # 得到最后一次数据（收盘数据）
        dapan.bomb = str(round(d["limit_up_broken_ratio"] * 100)) + "%"

        time.sleep(1)

        # ——涨停板个股——
        url = "https://flash-api.xuangubao.cn/api/pool/detail?pool_name=limit_up"
        if (date != datetime.now().date()):
            url += "&date=" + str(date)
        browser.get(url)
        page = str(browser.page_source)  # 得到页面源码
        page = page[page.find("{"):-20]
        ztlist = json.loads(page)["data"]
        for data in ztlist:
            if (data["stock_chi_name"].find("ST") < 0):
                slevel = data["limit_up_days"]
                # 创建涨停对象
                zt = xd.ZhangTing(data["stock_chi_name"], data["symbol"],
                                  (data["surge_reason"]["related_plates"][0]["plate_name"] if (
                                              data["surge_reason"] != None) else "无"),
                                  str(datetime.fromtimestamp(data["last_limit_up"]).time()),
                                  slevel, str(date))
                lianbanlist.append(zt)
                calc_lianban_amount(slevel)  # 计算连板数量

        time.sleep(1)
        browser.quit()

        # 保存数据
        save_to_sqlite()
        return True
    except Exception as e:
        print("出错了，\t", str(e))
        return False


#################################################

if __name__ == "__main__":
    get_today_data()