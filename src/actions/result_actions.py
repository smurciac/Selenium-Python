import re
import confvar

from src.pages import result_page as RP
from src.common import helpers as helper

def click_on_link(driver):
    _patrick_rothfuss_link = driver.find_element_by_xpath(RP.RESULTS)
    _patrick_rothfuss_link.click()
    _current_url = driver.current_url
    assert _current_url == confvar.PATRICK_ROTHFUSS_URL