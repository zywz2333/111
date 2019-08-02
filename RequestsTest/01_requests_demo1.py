# 1.在cmd中执行 pip3 install requests

import pymysql
import requests

def qurey(sql):
    '''
    这个方法是查询数据库用的
    '''
    dbinfo = {
        "host":"118.24.29.59",
        "user":"vn",
        "password":"1qaz!QAZ123",
        "db":"lux"
    }
    db = pymysql.connect(**dbinfo)  # 连接数据库
    cursor = db.cursor()  # 获取游标
    try:
        cursor.execute(sql)  # 执行SQL语句
        res = cursor.fetchall()  # 获取所有的返回值
        db.close()  # 关闭数据库连接
        return res
    except:
        return None

# http的get方
def test_get():
    res = requests.get("https://www.baidu.com")
    print(res.text) # 响应body
    print(res.status_code) # http响应状态码

# http的post之form-data方法
# postman转换成requests代码
def test_post_formdata():
    url = "http://132.232.44.158:7777/login"
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nwukun\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n123456\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    response = requests.request("POST", url, data=payload)
    print(response.text)

def test_post_json():
    # 接口地址
    url = "http://118.24.29.59:5000/userLogin/"
    # 请求的参数
    payload = {"username":"test", "password":"123456", "captcha":"123456"}
    # 使用post方法去请求这个接口
    response = requests.post(url=url, json=payload)
    
    # 判断http响应状态码
    # python自带的断言，assert,
    # 若果http响应状态码等于200，那么断言成功
    # 如果断言失败，assert就会抛出一个断言失败的异常，代码就终止
    assert response.status_code == 200

    # 判断接口返回的code值
    # response.json()把接口的响应值转成换字典，响应值必须要是json格式的，如果不是字典格式的就会报错
    assert response.json().get("code") == 200

    # 可选的，根据实际情况来绝对是不是需要去数据库查询
    sql = "select * from tbl_user where username='{}' and password='{}'".format("test", "123456")
    res = qurey(sql)
    print(res)
    # 如果res长度不为0 = 从数据库中查到了这条数据
    assert len(res) != 0   
    print("测试用例通过了！")


if __name__ == "__main__":
    # test_post_formdata()
    test_post_json()