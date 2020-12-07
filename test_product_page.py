from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = "http://selenium1py.pythonanywhere.com/accounts/login/"
		page = LoginPage(browser, link)
		page.open()
		email = str(time.time()) + "@fakemail.org"
		password = "pass99634"
		page.register_new_user(email, password)
		page.should_be_authorized_user()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.add_product_to_basket()
		product_page.solve_quiz_and_get_code()
		product_page.should_be_name_product_matches_product_in_basket()
		product_page.should_be_pirce_product_matches_price_basket()

	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.should_not_be_success_message()

		
class TestGuestFromProductPage():
	@pytest.mark.need_review
	def test_guest_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.add_product_to_basket()
		product_page.solve_quiz_and_get_code()
		product_page.should_be_name_product_matches_product_in_basket()
		product_page.should_be_pirce_product_matches_price_basket()

	@pytest.mark.need_review
	def test_guest_can_go_to_login_page_from_product_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
		page = ProductPage(browser, link)
		page.open()
		page.go_to_login_page()

	@pytest.mark.need_review
	def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
		page = ProductPage(browser, link)
		page.open()
		page.go_to_basket_page()
		basket_page = BasketPage(browser, browser.current_url)
		basket_page.should_be_empty_in_basket()
		basket_page.should_be_text_about_empty_basket()

	def test_guest_should_see_login_link_on_product_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
		page = ProductPage(browser, link)
		page.open()
		page.should_be_login_link()

	@pytest.mark.xfail(reason = "task: negative check")
	def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.add_product_to_basket()
		product_page.should_not_be_success_message()

	@pytest.mark.xfail(reason = "task: negative check")
	def test_message_disappeared_after_adding_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.add_product_to_basket()
		product_page.should_not_be_success_message_wiht_disappeared()



