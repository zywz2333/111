# 动态查找元素

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# 动态查找封装成一个方法
# 二次封装：以后，我们只需要通过调用它，传入对应的参数，就能实现动态查找
def find(driver, timeout, locator):
    from selenium.webdriver.support.ui import WebDriverWait                         # 这里是导入动态查找需要的第三方包
    element = WebDriverWait(w, timeout).until(lambda s: s.find_element(*locator))   # 实现元素的动态定位
    return element                                                                  # 返回已经查找的元素

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.maximize_window()
driver.get("https://www.baidu.com/")

# 动态查找
""" by id
search_input = ("id", "kw")
#e = WebDriverWait(driver, 10).until(lambda s: s.find_element(*search_input))
e = find(driver, 10, search_input)
e.send_keys("软件测试")

search_button = ("id", "su")
e1 = find(driver, 10, search_button)
e1.click()
"""

search_input = ("xpath", '//*[@id="kw"]')
search_button = ("xpath", '//*[@id="su"]')
find(driver, 10, search_input).send_keys("高级的自动化测试")
find(driver, 10, search_button).click



driver.quit()