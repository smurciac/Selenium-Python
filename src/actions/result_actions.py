import re

from src.pages import result_page as RP
from src.common import helpers as helper

def scroll_to_section(driver, section):
    _current_url = driver.current_url
    driver.get(_current_url + section)
    _checkbox_new_with_tags = driver.find_element_by_css_selector(RP.CHECKBOX_NEW_WITH_TAGS)
    _checkbox_new_with_tags.click()

def get_results(driver):
    _results = driver.find_element_by_css_selector(RP.RESULTS).text
    print(_results)

def order_by(driver):
    _order_by = driver.find_element_by_css_selector(RP.ORDER_BY)
    _order_by.click()
    _lowest_price = driver.find_element_by_css_selector(RP.LOWEST_PRICE)
    _lowest_price.click()

def assert_first_elements(driver):
    _result_item_1 = driver.find_element_by_css_selector(RP.RESULT_ITEM_1).text
    _result_item_2 = driver.find_element_by_css_selector(RP.RESULT_ITEM_2).text
    _result_item_3 = driver.find_element_by_css_selector(RP.RESULT_ITEM_3).text
    _result_item_4 = driver.find_element_by_css_selector(RP.RESULT_ITEM_4).text
    _result_item_5 = driver.find_element_by_css_selector(RP.RESULT_ITEM_5).text
    price_1 = helper.extract_and_print(_result_item_1)
    price_2 = helper.extract_and_print(_result_item_2)
    price_3 = helper.extract_and_print(_result_item_3)
    price_4 = helper.extract_and_print(_result_item_4)
    price_5 = helper.extract_and_print(_result_item_5)
    original_prices = [int(price_1), int(price_2), int(price_3), int(price_4), int(price_5)]
    assert original_prices == sorted(original_prices), "The prices weren't sorted as expected!"