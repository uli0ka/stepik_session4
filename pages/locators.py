from selenium.webdriver.common.by import By

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	FIELD_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
	FIELD_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
	FIELD_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
	BTN_REG = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
	BTN_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
	PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
	BASKET_PRICE = (By.CSS_SELECTOR, "p strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
	TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
	EMPTY_BASKET = (By.CSS_SELECTOR, ".col-sm-6.h3")
