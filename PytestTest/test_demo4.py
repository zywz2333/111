import time
import pytest
from selenium import webdriver


def test_selenium01():
    """
        pytest管理selenium测试用例，形成微型的测试框架
    """
    driver = webdriver.Chrome(executable_path="C:\\Users\\SNake\\VSCodeProjects\\ljtest201907\\SeleniumTest\\chromedriver.exe")
    driver.maximize_window()
    # 打开百度
    driver.get("https://www.baidu.com/")

    e = driver.find_element_by_id("kw")
    e.send_keys("pytest")

    e2 = driver.find_element_by_id("su")
    e2.click()

    time.sleep(3)
    assert driver.title == "pytest_百度搜索"

    driver.quit()

def test_morning_sx():
    """
        猫宁生鲜
    """
    driver = webdriver.Chrome(executable_path="C:\\Users\\SNake\\VSCodeProjects\\ljtest201907\\SeleniumTest\\chromedriver.exe")
    driver.maximize_window()

    driver.get("http://132.232.44.158:8080/login")
    
    driver.find_element_by_id("username").send_keys("13000000000")
    driver.find_element_by_id("password").send_keys("123456")
    driver.find_element_by_id("btnLogin").click()

    assert driver.title == "登录"

    driver.quit()