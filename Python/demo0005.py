
'''
import itchat

itchat.auto_login(hotReload=True)
friendlists = itchat.get_friends()
newlist = []
for friend in friendlists:
    newlist.append(friend["City"])
citydict = {}
for i in newlist:
    num = newlist.count(i)
    citydict[i] = num
print(citydict)
'''
'''
1、打开浏览器
2、打开百度的地址
3、输入需要搜索的内容
4、点击【百度一下】按钮
判断是不是搜索成功！

<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
<input type="submit" value="百度一下" id="su" class="btn self-btn bg s_btn">
'''
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="./drivers/chromedriver")  # 对谷歌浏览器进行实例化
driver.get("https://www.baidu.com")  # 在浏览器中输入网址


# driver.find_element_by_id("kw").send_keys("浪晋的测试小讲堂")  # 通过元素的ID来定位
# driver.find_element_by_name("wd").send_keys("浪晋")  # 同过元素的name来定位
# driver.find_element_by_class_name("s_ipt").send_keys("知乎")   # 通过class_name来定位
# driver.find_element_by_css_selector("input#kw.s_ipt").send_keys("260")  # 通过css_selector来定位
# driver.find_element_by_xpath("//*[@id=\"kw\"]").send_keys("2333")  # 通过xpath来定位
# driver.find_element_by_tag_name("input").send_keys("1111111")
driver.find_element_by_link_text("新闻").click()  # 通过超链接的文本来定位
driver.find_element_by_partial_link_text("退役军人工作会议代表").click()  # 通过超链接的部分文本来定位

driver.maximize_window()  # 最大化


ll = driver.window_handles  # 获取当前窗口所有的句柄

print(ll)
# time.sleep(3)
# driver.find_element_by_id("su").click()
time.sleep(2)
title = driver.title  # 获取title
if "浪晋的测试小讲堂_百度搜索" == title:
    print("测试通过！搜索成功！")
else:
    print("测试失败！")
driver.quit()  # 退出浏览器















