from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # This method waits until a web element is located and returns
    # True if it is displayed
    # locator_value is a param in order to received an xpath value
    def check_web_element_displayed(self, locator_value):
        try:
            return self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator_value))).is_displayed()
        except TimeoutError as e:
            print('ERROR!!! ' + str(e))
