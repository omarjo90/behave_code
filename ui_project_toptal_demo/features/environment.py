from browser import Browser
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.home_page import Homepage
from pages.shopping_cart_page import ShoppingCart


def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage(context.browser.driver)
    context.login_page = LoginPage(context.browser.driver)
    context.home_page = Homepage(context.browser.driver)
    context.shopping_cart_page = ShoppingCart(context.browser.driver)


def after_all(context):
    context.browser.close()
