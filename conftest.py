from selenium import webdriver

import confvar as confvar

def launch_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.get(confvar.URL)
    return driver