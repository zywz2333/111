"""
    py文件的作用：整个自动化测试项目框架的入口

    1. cases：用来放测试用例
    2. driver：用来放selenium驱动
    3. report：用来放测试报告
    4. utils：用来放工具代码（pymysql、htmltestrunner）
    5. run.py : 运行入口
"""
# 1. 导入所需的包
import unittest
from utils.HTMLTestRunner import HTMLTestRunner

# 2. 让unittest自动去查找cases下面所有测试w用例
testcases = unittest.defaultTestLoader.discover("cases", "test_*.py")

# 3. 把所有测试用例加载到测试集里面
testsuits = unittest.TestSuite()
testsuits.addTests(testcases)

# 4. 运行测试集并且生成测试报告
title = "测试报告"
descr = "猫宁生鲜的测试报告"
file_path = "./report/morning_reports.html"

with open(file_path, "wb") as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(testsuits)