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



if __name__ == "__main__":
    driver = get_driver()
    app = ("accessibility id", "App")
    search = ("accessibility id", "Search")

    find_element(driver, app).click()
    find_element(driver, search).click()

    # 返回上一级
    driver.back()

    # 点击home键
    driver.press_keycode(3)

    # 滑动 屏幕左滑（从左往右的手势）
    import time
    time.sleep(3)
    for a in range(10):
        driver.swipe(100, 640, 480, 640)