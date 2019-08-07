import pytest
import requests
from selenium import webdriver

class TestCaseTests():

    def test_morning_login(self):
        """
            猫宁登录失败的测试用例
        """
        driver = webdriver.Chrome(executable_path="C:\\Users\\SNake\\VSCodeProjects\\ljtest201907\\SeleniumTest\\chromedriver.exe")
        driver.maximize_window()
    
        driver.get("http://132.232.44.158:8080/login")
        
        driver.find_element_by_id("username").send_keys("13000000000")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("btnLogin").click()
    
        assert driver.title == "登录"
    
        driver.quit()

    def test_requests(self):
        """
            requests的测试方法
        """
        # 1. 构造请求
        response = requests.get("http://118.24.29.59:5000/")
        # 2. http响应状态断言
        assert response.status_code == 200
        # 3. 接口的返回值断言
        assert response.json().get("code") == 200
        # 4. 数据库查询
        pass