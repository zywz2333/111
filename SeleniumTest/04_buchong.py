from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.maximize_window()
driver.get("http://127.0.0.1:8080/demo/index.html")

# 通过父元素 查找子元素
f_div = driver.find_element_by_id("demo1")
# print(f_div.get_attribute("name")) 获取元素的属性
img = f_div.find_element_by_tag_name("img")
print(img.get_attribute("src"))


# 通过子元素查找父元素 : 挖坑
# s_img = driver.find_element_by_name("no1").parent

driver.quit()