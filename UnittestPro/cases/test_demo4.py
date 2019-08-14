"""
    unittest的生命周期
"""
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait                 # 这里是导入动态查找需要的第三方包

@unittest.skip("tiaoguo")
class TestCaseLifeCycle(unittest.TestCase):
    
    # 类方式和结束的方法，称为：类方法
    # 只执行一次
    # cls = self
    @classmethod
    def setUpClass(cls):
        # 初始化driver
        chrome_driver = "C:\\Users\\SNake\\VSCodeProjects\\ljtest201907\\SeleniumTest\\chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chrome_driver)
        cls.driver.maximize_window()
        
    @classmethod
    def tearDownClass(cls):
        # 退出测试
        cls.driver.quit()

    # 成员方法开始和结束的方法
    # 每一个test_开始的方法在运行前都会去执行setUp
    # 每一个test_开始的方法在结束后都会区执行teardown
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("teardown")
    
    def test_01_shopcar(self):
        self.driver.get("http://132.232.44.158:8080/")

        goods = ("xpath", '//*[@id="J_wrap_pro_add"]/li[1]/div[1]/a/img')
        join_shopcar = ("id", "J_mer_saleTag")
        js = ("xpath", '//*[@id="shopbox"]/div/div[2]/div/div/div[2]/p[2]/input')
        self.find_element(goods).click()
        self.find_element(join_shopcar).click()
        self.find_element(js).click()
        self.assertEqual(self.driver.title, "购物车")

    def test_02_login(self):
        self.driver.get("http://132.232.44.158:8080/login")

        username = ("id", "username")
        password = ("id", "password")
        login_btn = ("id", "btnLogin")
        self.find_element(username).send_keys("13000000000")
        self.find_element(password).send_keys("123456")
        self.find_element(login_btn).click()

        self.assertEqual(self.driver.title, "登录")

    def find_element(self, locator, timeout=10):
        """
            查找单个元素
                参数：locator=("id", "123")
                类型：
                ID = "id"
                XPATH = "xpath"
                LINK_TEXT = "link text"
                PARTIAL_LINK_TEXT = "partial link text"
                NAME = "name"
                TAG_NAME = "tag name"
                CLASS_NAME = "class name"
                CSS_SELECTOR = "css selector"
        """
        return WebDriverWait(self.driver, timeout).until(lambda s: s.find_element(*locator))

if __name__ == "__main__":
    unittest.main()