import requests
import json


#理杏仁请求基础信息
#token   2b95ad00-8881-4a1d-9d87-b124ca63b31f
request_url="https://open.lixinger.com/api/a/stock"
body={"token": "2b95ad00-8881-4a1d-9d87-b124ca63b31f","industryType": "bank"}
headers = {'content-type': "application/json"}
response = requests.post(request_url, body,headers)

#字符串转换为json并取data值
print("text:",json.loads(response.text)['data'])
print("status:",response.status_code)