import requests
from utils.exceltools import read_excel
from utils.dbtools import query

# 1. 准备测试用例，测试用例放在excel中
# [[1,测试用例1,...], [2,测试用例2,...]]
"""
    1. 准备了接口测试用例文档
    2. 实现了接口测试的读取excel功能
"""

# 2. 读取excel，获取所有的测试用例
testcases = read_excel("testcases/接口测试用例模板.xlsx", "Sheet1")

# 3. 使用自动代码去执行这些测试用例
for testcase in testcases:
    # 3.1 构造请求
    # 这些值都是从我们自己定义的excel中读取的
    url = testcase[1]   # 接口的地址
    method = testcase[5] # 请求的方法
    playload = eval(testcase[7]) # 请求的参数
    case_name = testcase[3] # 测试用例的名字
    http_response_code = int(testcase[8]) # http响应状态码预期结果
    interface_status_code = int(testcase[9]) # 接口的code预期结果
    request_sql = testcase[10]
    try:
        res = requests.request(method, url=url, json=playload)
        # 3.2 断言http响应状态
        assert res.status_code == http_response_code
        # 3.3 断言接口的响应值
        assert res.json().get("code") == interface_status_code
        # 3.4 去数据库中判断是否存在这个账号和密码
        ri = query(request_sql)
        assert len(ri) != 0
        print("【{}】执行通过".format(case_name))
    except:
        print("【{}】执行失败".format(case_name))

