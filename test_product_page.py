from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

#@pytest.mark.parametrize('link', [0,1,2,3,4,5,6,
#                                  pytest.param(7, marks=pytest.mark.xfail),
#                                  8,9])
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#def test_guest_can_add_product_to_basket(browser, link):
#	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
#	product_page = ProductPage(browser, link)
#	product_page.open()
#	product_page.add_product_to_basket()
#	product_page.solve_quiz_and_get_code()
#	product_page.should_be_name_product_matches_product_in_basket()
#	product_page.should_be_pirce_product_matches_price_basket()

@pytest.mark.xfail(reason = "task: negative check")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_product_to_basket()
	product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.should_not_be_success_message()

@pytest.mark.xfail(reason = "task: negative check")
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_product_to_basket()
	product_page.should_not_be_success_message_wiht_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_basket_page()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.should_be_empty_in_basket()
	basket_page.should_be_text_about_empty_basket()