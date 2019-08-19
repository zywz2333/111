import re
import requests


def get_params(ld, rd, data, status=1):
    """
        关联函数，根据左边界和有边界来实现获取参数
    """
    flag = re.compile(ld+"(.*?)"+rd)
    res = re.findall(flag, data)
    if len(res) == 1:
        return res[0]
    else:
        if status == 1:
            return res[0]
        else:
            return res

# 1. 先去登录
url = "http://132.232.44.158:5000/userLogin/"
payload = {"username":"test", "password":"123456", "captcha":"123456"}
res = requests.post(url, json=payload)
# token = response.json()["data"]["token"]
# 第二个万能的方法， re模块
token = get_params('.*token": "', '"', res.text)

# 2. 收藏文章
url = "http://132.232.44.158:5000/articleCollect/"
payload = {'articleId':1, 'token': token}
response = requests.post(url, json=payload, cookies = res.cookies)

print(response.text)