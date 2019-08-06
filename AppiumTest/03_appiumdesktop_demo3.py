# 导入所需要的依赖包
from appium import webdriver


# 打开被测的app
desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '7.1.2'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'Redmi 4X'                     # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'io.appium.android.apis'       # app的名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['appActivity'] = '.ApiDemos'                   # app的启动页名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘

# 解锁手机并且去打开app
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# 去点点点
# by id   > resouceid
# e = driver.find_element_by_id("android:id/text1")
# e.click()

# xpath > xpath 
# e1 = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Accessibility Node Provider"]')
# e1.click()

# accessibility_id
app = driver.find_element_by_accessibility_id("App")
app.click()

# 文本值：new UiSelector().text("这里写文本值"): 文本值是非常好用的
app_search = driver.find_element_by_android_uiautomator('new UiSelector().text("Search")')
app_search.click()  

app_search_invoke = driver.find_element_by_accessibility_id("Invoke Search")
app_search_invoke.click()

# 输入
query = driver.find_element_by_id("io.appium.android.apis:id/txt_query_prefill")
query.send_keys("你好佩奇")

app_data = driver.find_element_by_id("io.appium.android.apis:id/txt_query_appdata")
driver.set_value(app_data, "hello peiqi!")

app_data.clear()

start_search_btn = driver.find_element_by_id("io.appium.android.apis:id/btn_start_search")
print(start_search_btn.text)


# 退出
driver.quit()

