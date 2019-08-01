from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.maximize_window()
driver.get("http://118.24.29.59:8080")

e = driver.find_element_by_xpath('//*[@id="J_wrap_pro_add"]/li[1]/div[1]/a/img')
e.click()

e1 = driver.find_element_by_id("J_mer_saleTag")
e1.click()

e2 = driver.find_element_by_link_text("购物袋")
e2.click()


driver.quit()