import time
import unittest
from selenium import webdriver

class TestCaselogin(unittest.TestCase):
    """
        登录相关的测试用例
    """   
    @classmethod
    def setUpClass(cls):
        """
            开始执行打开网页
        """
        chrome = "C:\\Users\\SNake\\VSCodeProjects\\ljtest201907\\UnittestProAagin\\driver\\chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chrome)
        cls.driver.maximize_window()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        """
            每次都去打开登陆页面
        """
        self.driver.get("http://132.232.44.158:8080/login")
        
    
    def test_01_login_success(self):
        """
            登录成功
        """
        self.driver.find_element_by_id("username").send_keys("13000000011")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("btnLogin").click()

        time.sleep(3)
        title = self.driver.title
        self.assertEqual(title, "首页")

    def test_02_login_failed(self):
        """
            登录失败
        """
        self.driver.find_element_by_id("username").send_keys("13000000011")
        self.driver.find_element_by_id("password").send_keys("1234567")
        self.driver.find_element_by_id("btnLogin").click()

        time.sleep(3)
        title = self.driver.title
        self.assertEqual(title, "登录")