"""
    百度的首页pageobject
"""
from utils.seleniumtools import find_element

class BaiduIndex():
    # 1. 搜索框和搜索按钮的元素
    def __init__(self, driver):
        self.driver = driver
        self.search_input = ("id", "kw")
        self.search_button = ("id", "su")

    # 2. 把操作操作步骤封装成方法

    # 2.1 打开百度首页
    def open_baidu_index(self):
        self.driver.get("https://www.baidu.com/")

    # 2.2 搜索方法
    def search_kw(self):
        find_element(self.driver, self.search_input).send_keys("123")
        find_element(self.driver, self.search_button).click()