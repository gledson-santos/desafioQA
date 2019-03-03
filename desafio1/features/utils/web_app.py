from selenium import webdriver


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def get_driver(self):
        return self.driver

    def go_site(self, url):
        self.driver.get(url)


webapp = WebApp.get_instance()
