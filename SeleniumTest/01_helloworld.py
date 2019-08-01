import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get("https://www.baidu.com")

e = driver.find_element_by_id("kw")
e.send_keys("自动化测试")

# 2. 静态查找：网页加载过慢，都会导致查找元素出错
e1 = driver.find_element_by_id("su")
e1.click()

# 1. 静态等待
time.sleep(3)

print(driver.title)
if driver.title == "自动化测试_百度搜索":
    print("测试用例通过了！")
else:
    print("测试用例失败了！")