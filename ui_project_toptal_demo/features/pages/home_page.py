from .base_page import BasePage
from selenium.webdriver.common.by import By


class Homepage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Web Element Locators
    open_menu_button = "//button[contains(text(), 'Open Menu')]"
    sort_container = "//select[@class='product_sort_container']"

    # Web elements to add in the shopping cart
    first_add_to_cart_button = "(//div[@class='inventory_container']//button)[1]"
    second_add_to_cart_button = "(//div[@class='inventory_container']//button)[2]"
    shopping_cart = 'shopping_cart_container'

    # Left principal menu
    left_principal_menu = "//button[contains(text(), 'Open Menu')]"
    all_items_option = "inventory_sidebar_link"

    # Sort container options
    z_to_a_option = "//option[@value='za']"
    low_to_high_option = "//option[@value='lohi']"
    high_to_low_option = "//option[@value='hilo']"

    # XPATH's expected texts after sorting options
    after_sort_z_to_a_expected_text = '(//div[@data-test="inventory-item-name"])[1]'
    after_sort_low_to_high_expected_text = '(//div[@data-test="inventory-item-name"])[1]'
    after_sort_high_to_low_expected_text = '(//div[@data-test="inventory-item-name"])[1]'

    # Methods that perform home page actions

    # This method clicks on the first add to cart button element displayed in the UI
    # and add it to the shopping cart
    def click_first_add_to_cart_button(self):
        self.driver.find_element(By.XPATH, self.first_add_to_cart_button).click()

    # This method clicks on the second add to cart button element displayed in the UI
    # and add it to the shopping cart
    def click_second_add_to_cart_button(self):
        self.driver.find_element(By.XPATH, self.second_add_to_cart_button).click()

    # This method click on shopping cart icon
    def click_shopping_cart(self):
        self.driver.find_element(By.ID, self.shopping_cart).click()

    # This method returns the Webdriver to the home page
    def go_to_home_page(self):
        self.check_web_element_displayed(self.left_principal_menu)

        self.driver.find_element(By.XPATH, self.left_principal_menu).click()
        self.driver.find_element(By.ID, self.all_items_option).click()
        # self.wait.until(EC.element_to_be_clickable(By.ID("react-burger-cross-btn")))
        # self.driver.find_element(By.ID, 'react-burger-cross-btn').click()

    # This method returns the Webdriver to the shopping cart page
    def go_to_shopping_cart_page(self):
        self.driver.find_element(By.ID, self.shopping_cart).click()

    # This method select the option to sort and search elements from Z to A
    def select_z_to_a_option(self):
        self.driver.find_element(By.XPATH, self.z_to_a_option).click()

    # This method select the option to sort and search elements from low to high price
    def select_low_to_high_option(self):
        self.driver.find_element(By.XPATH, self.low_to_high_option).click()

    # This method select the option to sort and search elements from high to low price
    def select_high_to_low_option(self):
        self.driver.find_element(By.XPATH, self.high_to_low_option).click()

    # This method verifies that sorting using Z to A works as expected
    def check_z_to_a_sort_works(self):
        self.check_web_element_displayed(self.after_sort_z_to_a_expected_text)
        return self.driver.find_element(By.XPATH, self.after_sort_z_to_a_expected_text).text

    # This method verifies that sorting using low to high price works as expected
    def check_low_to_high_sort_works(self):
        self.check_web_element_displayed('//*[@id="react-burger-cross-btn"]')
        self.driver.find_element(By.ID, 'react-burger-cross-btn').click()

        return self.driver.find_element(By.XPATH, self.after_sort_low_to_high_expected_text).text

    # This method verifies that sorting using high to low price works as expected
    def check_high_to_low_sort_works(self):
        return self.driver.find_element(By.XPATH, self.after_sort_high_to_low_expected_text).text

    # This method clicks on left principal menu in order to open it and displays its options
    def click_menu_button(self):
        self.driver.find_element(By.XPATH, self.left_principal_menu).click()

    # This method clicks on logout button
    def click_logout_button(self):
        self.driver.find_element(By.ID, 'logout_sidebar_link').click()







