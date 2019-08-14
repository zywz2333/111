import unittest
from selenium import webdriver
from po.baiduindex import BaiduIndex


class TestCaseBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_driver = "C:\\Users\\SNake\\VSCodeProjects\\ljtest201907\\SeleniumTest\\chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=chrome_driver)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_search(self):
        # 打开百度首页
        baidu = BaiduIndex(self.driver)
        baidu.open_baidu_index()
        baidu.search_kw()