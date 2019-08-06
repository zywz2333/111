from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def get_driver(pv="7.1.2", dn="Redmi 4X", ap="io.appium.android.apis", aa=".ApiDemos"):
    """
        传入对应的参数去打开手机app,并且去返回这个driver对象
    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'            # 打开什么平台的app，固定的 > 启动安卓平台
    desired_caps['platformVersion'] = pv                # 安卓系统的版本号：adb shell getprop ro.build.version.release
    desired_caps['deviceName'] = dn                     # 手机/模拟器的型号：adb shell getprop ro.product.model
    desired_caps['appPackage'] = ap                     # app的名字：adb shell dumpsys activity | findstr "mFocusedActivity"
    desired_caps['appActivity'] = aa                    # app的启动页名字：adb shell dumpsys activity | findstr "mFocusedActivity"
    desired_caps['unicodeKeyboard'] = True              # 为了支持中文
    desired_caps['resetKeyboard'] = True                # 设置成appium自带的键盘

    # 解锁手机并且去打开app
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver

def find_element(driver, locator):
    """
        传入locator = ("id", "id->value")
        id: "id"
        xpath: "xpath"
        accessibility_id: "accessibility id"
        android_uiautomator: "-android uiautomator"
    """
    return WebDriverWait(driver, 30).until(lambda s: s.find_element(*locator))

def click(driver, locator):
    """
        元素点击方法
    """
    find_element(driver, locator).click()

if __name__ == "__main__":
    # 打开app，获得driver
    driver = get_driver()
    ay = ("id", "android:id/text1")
    cv = ("xpath", '//android.widget.TextView[@content-desc="Custom View"]')
    click(driver, ay)
    click(driver, cv)

    # find_element(driver, ay).click()
    # find_element(driver, cv).click()

    # id
    #accessibility = ("id", "android:id/text1") 
    #acce = find_element(driver, accessibility)  
    #acce.click()
    # xpath
    #custom_view = ("xpath", '//android.widget.TextView[@content-desc="Custom View"]')
    #cv = find_element(driver, custom_view)
    #cv.click()
    
    # accessibility id
    #content = ("accessibility id", "Content")
    #e = find_element(driver, content)
    #e.click()

    # 文本值查找
    #package = ("-android uiautomator", 'new UiSelector().text("Packages")')
    #e2 = find_element(driver, package)
    #e2.click()
