import unittest
from utils.util_date import get_now
from utils.HTMLTestRunner import HTMLTestRunner

testcase = unittest.defaultTestLoader.discover("./case", "test_*.py")
testsuit = unittest.TestSuite()
testsuit.addTests(testcase)

title = "测试报告"
descr = "猫宁生鲜测试报告"
filepath = "./report/morning-{}.html".format(get_now())
with open(filepath, "wb") as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(testsuit)