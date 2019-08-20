import unittest
from selenium import webdriver
from po.page_login import LoginPage

class TestCaseLoginPO(unittest.TestCase):
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

    def test_01_login_success(self):
        """
            登录成功
        """
        login = LoginPage(self.driver)                          # 初始化po
        login.open_login_page()                                 # 打开页面
        login.login("13000000011", "123456")                    # 登录
        self.assertNotEqual(self.driver.title, login.title)     # 判断登录成功后页面的标题不是登录页面的标题