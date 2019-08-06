# 导入所需要的依赖包
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

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


"""
    id: "id"
    xpath: "xpath"
    accessibility_id: "accessibility id"
    android_uiautomator: "-android uiautomator"
"""

# 动态查找：id
locator = ("id", "android:id/text1")
e = WebDriverWait(driver, 30).until(lambda s: s.find_element(*locator))
e.click()

locator2 = ("xpath", '//android.widget.TextView[@content-desc="Accessibility Node Provider"]')
e = WebDriverWait(driver, 30).until(lambda s: s.find_element(*locator2))
e.click()