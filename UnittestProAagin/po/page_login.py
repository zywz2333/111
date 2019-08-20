from utils.util_selenium import find_element

class LoginPage():

    def __init__(self, driver):
        """
            构造方法
        """
        self.driver = driver
        self.username = ("id", "username")
        self.password = ("id", "password")
        self.btnlogin = ("id", "btnLogin")

        self.title = "登录"
        self.url = "http://132.232.44.158:8080/login"

    def open_login_page(self):
        """
            打开登录页面
        """
        self.driver.get(self.url)

    def login(self, account, password):
        """
            登录
        """
        find_element(self.driver, self.username).send_keys(account)
        find_element(self.driver, self.password).send_keys(password)
        find_element(self.driver, self.btnlogin).click()