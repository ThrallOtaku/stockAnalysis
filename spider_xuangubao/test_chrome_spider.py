from selenium import webdriver
from _datetime import datetime
import time, json


date=datetime.now().date()
chrome_driver=r"D:\python\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
browser=webdriver.Chrome(executable_path=chrome_driver)
# chrome_options = webdriver.chrome.options.Options()
# chrome_options.add_argument("--headless")
# browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome()
# ——大盘涨跌数量——
url = "https://flash-api.xuangubao.cn/api/market_indicator/line?fields=rise_count,fall_count"
if (date != datetime.now().date()):
    url += "&date=" + str(date)
browser.get(url)
page = str(browser.page_source)  # 得到大盘涨跌数据
page = page[page.find("{"):-20]
data = json.loads(page)["data"]
print(data)
if (len(data) <= 0):
    print("没有" + str(date) + "的数据")
