import requests

#API接口IP即api.weixin.qq.com的解析地址
url = "https://api.weixin.qq.com/cgi-bin/get_api_domain_ip"

params = {"access_token":"31_fsCDKkadzuBBi8EkG0Aq0sHDvHHdRa5lQv0gGH2hZ1ZNrXmeLhbxX2IS2sp9N_pDasjF5MTjXnXwKm3nwAtuTTSrYoJsIdR0mvMSSloMa2raibQz0kADIgpBDsGnSOQKcnViXOXsMPF8fpZRQLNiADAHCE"}

res = requests.get(url=url,params=params)

print(res.text)