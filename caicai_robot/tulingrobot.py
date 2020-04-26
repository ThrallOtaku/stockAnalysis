import requests
import json
key = 'b8c7edd455f144d783a967ca37d51e0c'
while True:
    info = input('我：')
    url = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+info
    res = requests.get(url)
    res.encoding = 'utf-8'
    jd = json.loads(res.text)
    print('Tuling: '+jd['text'])


