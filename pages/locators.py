from selenium.webdriver.common.by import By

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	BTN_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
	PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
	BASKET_PRICE = (By.CSS_SELECTOR, "p strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasketPageLocators():
	BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
	TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
	EMPTY_BASKET = (By.CSS_SELECTOR, ".col-sm-6.h3")
