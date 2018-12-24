import time

from src.pages import home_page as HP

def search(driver, item_to_seach):
    _english_option = driver.find_element_by_css_selector(HP.ENGLISH_OPTION)
    _english_option.click()
    _search_bar = driver.find_element_by_css_selector(HP.SEARCH_BAR)
    _search_bar.send_keys(item_to_seach)
    if item_to_seach.find("wind") is not -1:
        _search_button = driver.find_element_by_css_selector(HP.SEARCH_BUTTON)
        _search_button.click()
        time.sleep(3)
    else:
        time.sleep(1)
        _first_element_on_list = driver.find_element_by_css_selector(HP.FIRST_ELEMENT_ON_LIST)
        _first_element_on_list.click()
        time.sleep(3)