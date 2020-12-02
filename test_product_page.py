from .pages.product_page import ProductPage
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

