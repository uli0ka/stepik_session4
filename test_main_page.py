from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
	def test_guest_can_go_to_login_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/"
		page = MainPage(browser, link)
		page.open()
		page.should_be_login_link()
		page.go_to_login_page()
		page = LoginPage(browser, browser.current_url)
		page.should_be_login_page()
    
	def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/"
		page = MainPage(browser, link)
		page.open()
		page.go_to_basket_page()
		page = BasketPage(browser, browser.current_url)
		page.should_be_empty_in_basket()
		page.should_be_text_about_empty_basket()

