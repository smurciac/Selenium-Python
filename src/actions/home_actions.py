import time

from src.pages import home_page as HP

def search(driver):
    _search_bar = driver.find_element_by_css_selector(HP.SEARCH_BAR)
    _search_bar.send_keys("PUMA")
    _search_button = driver.find_element_by_css_selector(HP.SEARCH_BUTTON)
    _search_button.click()
    time.sleep(3)