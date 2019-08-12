"""
    unittest自带的断言，只有当用到unittest框架来组织测试用例的时候，才使用self.assertXXXX的来断言
    除此之外，老老实实用python自带的assert断言
"""

import unittest

class TestCaseAssert(unittest.TestCase):
    
    def test_01_xiangdeng(self):
        # 判断相等
        a = 0
        b = 1
        self.assertNotEqual(a, b) # 如果a！=b，通过；反之失败
        self.assertEqual(a, b, "a和b不相等") # 第三个参数是可传可不传，如果a!=b，那么就会断言失败，并且输出msg

    def test_02_zhenjia(self):
        self.assertTrue(True)  # True通过，False失败
        self.assertFalse(False)# False通过，True失败

    # 用得很少
    def test_03_is(self):
        a = "小强强"
        b = "小坤坤"
        self.assertIsNot(a, b) # a和b不是同一个对象，就通过；反之失败
        self.assertIs(a, b)     # a和b是同一个对象就通过；反之失败
    
    def test_04_isnone(self):
        a = None
        b = ""
        self.assertIsNone(a) # 为None通过，反之失败
        self.assertIsNotNone(b) # 不为None通过，反之失败
        
    def test_04_in(self):
        """
            a = "中国香港"
            b = "中香"
            b in a
            False
        """
        a = "小坤坤"
        b = "坤坤"
        c = "小小坤"
        self.assertIn(b, a) # b在a里面能找到，就通过；反之失败
        self.assertNotIn(c, a) # c不在a里面就通过；反之失败
        # self.assertIsInstance() # 是否为实例对象
        # self.assertIsNotInstance() # 是否为实例对象


if __name__ == "__main__":
    unittest.main()