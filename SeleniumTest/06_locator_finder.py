from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def is_elemenet_exist(driver, locator):
    """
        判断元素是否存在
    """
    try:
        WebDriverWait(driver, 10).until(lambda s: s.find_element(*locator))
        return True
    except:
        return False

driver =webdriver.Chrome(executable_path="./chromedriver.exe")
driver.maximize_window()
driver.get("http://132.232.44.158:8080/morning/user/userLogin")

driver.find_element_by_id("adminNo").send_keys("123")
driver.find_element_by_id("password").send_keys("123")
driver.find_element_by_id("btn_login").click()

locator = ("xpath", '//*[@id="verifyCheck"]/div/div[1]/label')
assert is_elemenet_exist(driver, locator) is True

driver.quit()