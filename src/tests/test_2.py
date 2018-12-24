import conftest as conftest
import confvar

from src.actions import home_actions as HA
from src.actions import result_actions as RA
from src.pages import home_page as HP
from src.pages import result_page as RP
from selenium.webdriver.common.keys import Keys

def user_can_search_by_using_suggestions():
    driver = conftest.launch_driver()
    HA.search(driver, confvar.PARTIAL_SEARCH)
    RA.click_on_link(driver)
    driver.close()