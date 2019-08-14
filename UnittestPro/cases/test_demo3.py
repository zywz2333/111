"""
    unittest的测试结果
"""

import unittest


@unittest.skip("tiaoguo")
class TestCaseResultDemo(unittest.TestCase):
    def test_01_pass(self):
        # pass 所有代码都执行完了/断言通过
        self.assertEqual(1, 1)
    
    def test_02_failed(self):
        # 断言失败了
        self.assertEqual(1, 2)
    
    def test_03_error(self):
        # 代码报错了抛出了异常
        nums = [123,1,2]
        nums[4]

if __name__ == "__main__":
    # 这种写法通常用来调试脚本
    unittest.main()