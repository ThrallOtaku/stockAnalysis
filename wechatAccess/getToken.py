import requests

#微信限制请求，用token控制,请求微信公众号token，token两小时之内有效，如果超过两个小时就要重新申请
#https请求方式: GET https://api.weixin.qq.com/cgi-bin/token?appid=APPID&secret=APPSECRET
url = "https://api.weixin.qq.com/cgi-bin/token"

params = {"grant_type":"client_credential","appid":"wx0cb7082e546e6c64","secret":"f658a666b8fca9f2f6ac13b0c0d79abb"}

res = requests.get(url=url,params=params)

# 31_fsCDKkadzuBBi8EkG0Aq0sHDvHHdRa5lQv0gGH2hZ1ZNrXmeLhbxX2IS2sp9N_pDasjF5MTjXnXwKm3nwAtuTTSrYoJsIdR0mvMSSloMa2raibQz0kADIgpBDsGnSOQKcnViXOXsMPF8fpZRQLNiADAHCE
print(res.text)