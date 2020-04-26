import requests
import json

#理杏仁请求财报数据
#token   2b95ad00-8881-4a1d-9d87-b124ca63b31f
request_url="https://open.lixinger.com/api/a/indice/fs"
body={"token": "2b95ad00-8881-4a1d-9d87-b124ca63b31f","date": "2017-09-30","stockCodes": ["600016","601398"],"metrics": ["q.profitStatement.toi.t"]}
headers = {'content-type': "application/json"}

response = requests.post(request_url, body,headers)

print("status:",response.status_code)
print("text:",response.text)
