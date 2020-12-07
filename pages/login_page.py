from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Word 'login' was not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.FIELD_EMAIL)
        input_email.send_keys(email)
        input_password1 = self.browser.find_element(*LoginPageLocators.FIELD_PASS1)
        input_password1.send_keys(password)
        input_password2 = self.browser.find_element(*LoginPageLocators.FIELD_PASS2)
        input_password2.send_keys(password)
        btn_reg = self.browser.find_element(*LoginPageLocators.BTN_REG)
        btn_reg.click()

        

