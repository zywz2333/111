   
from selenium.webdriver.support.ui import WebDriverWait                 # 这里是导入动态查找需要的第三方包
   
def find_element(driver, locator, timeout=10):
    """
        查找单个元素
            参数：locator=("id", "123")
            类型：w
            ID = "id"
            XPATH = "xpath"
            LINK_TEXT = "link text"
            PARTIAL_LINK_TEXT = "partial link text"
            NAME = "name"
            TAG_NAME = "tag name"
            CLASS_NAME = "class name"
            CSS_SELECTOR = "css selector"
    """
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))