from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.maximize_window()
driver.get("https://passport2.eastmoney.com/pub/login")

# 找到iframe
iframe = driver.find_element_by_id("frame_login")
# 直接去找就会报错
# driver.find_element_by_id("txt_account").send_keys("123")

# driver作用域切换到iframe里面
driver.switch_to_frame(iframe)
driver.find_element_by_id("txt_account").send_keys("123")

# 作用域在小网页时，不能去操作大网页的元素
# driver.find_element_by_link_text("点此进入基金交易").click()
# 在操作完小网页之后，需要把作用域切换到大网页里面
driver.switch_to_default_content()
driver.find_element_by_link_text("点此进入基金交易").click()
