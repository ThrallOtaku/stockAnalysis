import requests

#click和view的请求示例
ACCESS_TOKEN="31_fsCDKkadzuBBi8EkG0Aq0sHDvHHdRa5lQv0gGH2hZ1ZNrXmeLhbxX2IS2sp9N_pDasjF5MTjXnXwKm3nwAtuTTSrYoJsIdR0mvMSSloMa2raibQz0kADIgpBDsGnSOQKcnViXOXsMPF8fpZRQLNiADAHCE"
url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token="+ACCESS_TOKEN

params = {
          "button": [
              {
                  "type": "click",
                  "name": "今日歌曲",
                  "key": "V1001_TODAY_MUSIC"
              },
              {
                  "name": "菜单",
                  "sub_button": [
                      {
                          "type": "view",
                          "name": "搜索",
                          "url": "http://www.soso.com/"
                      },
                      {
                          "type": "miniprogram",
                          "name": "wxa",
                          "url": "http://mp.weixin.qq.com",
                          "appid": "wx286b93c14bbf93aa",
                          "pagepath": "pages/lunar/index"
                      },
                      {
                          "type": "click",
                          "name": "赞一下我们",
                          "key": "V1001_GOOD"
                      }]
              }]
          }

res = requests.post(url=url,data=params)

print(res.text)