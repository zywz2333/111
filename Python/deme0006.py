from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
driver.get("http://118.24.29.59:8080/morning/")
driver.find_element_by_link_text("登录").click()
time.sleep(3)
driver.find_element_by_name("user.loginName").send_keys("106@qq.com")
driver.find_element_by_name("user.loginPassword").send_keys("a123456")
driver.find_element_by_id("btn_login").click()
time.sleep(3)
driver.find_element_by_class_name("mian-nav-right-user").click()
driver.find_element_by_link_text("个人中心").click()
time.sleep(3)


winlist = driver.window_handles  # 获取所有的句柄
print(winlist)
windowname = driver.current_window_handle  # 获取当前句柄
print("第一个窗口：",windowname)
driver.switch_to.window(winlist[1])  # 切换句柄
windowname = driver.current_window_handle  # 获取当前句柄
print("第二个窗口：",windowname)


time.sleep(4)
# driver.find_element_by_name("loginName").send_keys("哈哈哈")

# driver.find_element_by_class_name("btn btn-info subbtn").click()

# driver.find_element_by_class_name("btn btn-info subbtn").send_keys(Keys.ENTER)



driver.quit()