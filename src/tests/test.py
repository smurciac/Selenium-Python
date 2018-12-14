import conftest as conftest

from src.actions import home_actions as HA
from src.actions import result_actions as RA
from src.pages import home_page as HP
from src.pages import result_page as RP
from selenium.webdriver.common.keys import Keys

driver = conftest.launch_driver()
HA.search(driver)
RA.scroll_to_section(driver, RP.CONDITION)
RA.get_results(driver)
RA.order_by(driver)
RA.assert_first_elements(driver)
driver.close()