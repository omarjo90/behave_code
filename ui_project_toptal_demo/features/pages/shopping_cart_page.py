from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ShoppingCart(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    cart_quantity = "//div[@class='cart_quantity']"
    remove_button = "(//button[contains(text(), 'Remove')])"
    shopping_counter = "//span[@class='shopping_cart_badge']"
    checkout_button = "checkout"

    # Methods that perform shopping cart page actions
    # This method removes one item from the shopping cart
    def remove_item_from_shopping_cart(self):
        self.driver.find_element(By.XPATH, self.remove_button).click()

    # This method validates if after removing one item, the number of elements
    # is = to 1, because previously 2 items were added, so when this method is executed
    # only one item should remain in the list
    def check_item_was_removed(self):
        if self.driver.find_element(By.XPATH, self.shopping_counter).text == str(1):
            return True

    # This method validates that second item was added to the shopping cart
    def check_second_item_added(self):
        return 'Sauce Labs Bike Light' in self.driver.page_source

    # This method clicks checkout button
    def click_checkout_button(self):
        self.driver.find_element(By.ID, self.checkout_button).click()

    # This method validates that the 3 fields for checking out the item, are displayed
    def check_labels_to_checkout_displays(self):
        return self.driver.find_element(By.ID, 'first-name').is_displayed() and self.driver.find_element(By.ID,
            'last-name').is_displayed() and self.driver.find_element(By.ID, 'postal-code').is_displayed()

    # This method fills up the 3 required fields to checkout the order
    def fill_checkout_information(self):
        self.driver.find_element(By.ID, 'first-name').send_keys('Omar')
        self.driver.find_element(By.ID, 'last-name').send_keys('Guzman')
        self.driver.find_element(By.ID, 'postal-code').send_keys('05050')

    # This method clicks on continue button to checkout the order
    def click_continue_button_to_checkout(self):
        self.driver.find_element(By.ID, "continue").click()

    # This methods verifies if the amount of the order is correct,
    # and delivery company text is displayed
    def overview_order(self):
        return 'Free Pony Express Delivery!' in self.driver.page_source and '10.79' in self.driver.page_source

    # This method click finish checkout button
    def click_finish_button(self):
        self.driver.find_element(By.ID, "finish").click()

    # This method verifies if the order was successfully dispatched
    # also has 2 variables in order to compare the expected UI text again
    # the text returned from the web element
    def check_order_dispatched(self):
        expected_text = 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
        web_element_text = self.driver.find_element(By.XPATH, "//*[@class='complete-text']").text
        return web_element_text == expected_text
