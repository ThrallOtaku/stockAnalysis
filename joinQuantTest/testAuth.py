from jqdatasdk import *

id='18518326872'
password='84559515A'
auth(id,password)
# 查询是否连接成功
is_auth = is_auth()
print('is_auth:',is_auth)

count=get_query_count()
print(count)

