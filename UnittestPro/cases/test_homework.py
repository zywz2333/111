import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait                 # 这里是导入动态查找需要的第三方包

class TestCaseMorning(unittest.TestCase):
    def test_01_shopcar(self):
        chrome_driver = "C:\\Users\\SNake\\VSCodeProjects\\ljtest201907\\SeleniumTest\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        driver.maximize_window()
        driver.get("http://132.232.44.158:8080/")

        goods = ("xpath", '//*[@id="J_wrap_pro_add"]/li[1]/div[1]/a/img')
        join_shopcar = ("id", "J_mer_saleTag")
        js = ("xpath", '//*[@id="shopbox"]/div/div[2]/div/div/div[2]/p[2]/input')
        self.find_element(driver, 10, goods).click()
        self.find_element(driver, 10, join_shopcar).click()
        self.find_element(driver, 10, js).click()
        self.assertEqual(driver.title, "购物车")
        driver.quit()
    
    def test_02_login(self):
        chrome_driver = "C:\\Users\\SNake\\VSCodeProjects\\ljtest201907\\SeleniumTest\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        driver.maximize_window()
        driver.get("http://132.232.44.158:8080/")

        self.find_element(driver, 10, ("id", "username")).send_keys("123123")
        self.find_element(driver, 10, ("id", "password")).send_keys("123123")
        self.find_element(driver, 10, ("id", "btnLogin")).click()

        driver.quit()

         

    def find_element(self, driver, timeout, locator):
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
        element = WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))  # 实现元素的动态定位
        return element    

if __name__ == "__main__":
    unittest.main()