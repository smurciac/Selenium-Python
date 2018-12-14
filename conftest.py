from selenium import webdriver

import confvar as confvar

def launch_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(confvar.URL)
    return driver