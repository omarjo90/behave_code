from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            cls._instance.driver.implicitly_wait(15)
            cls._instance.driver.maximize_window()
        return cls._instance

    def close(self):
        self.driver.quit()
