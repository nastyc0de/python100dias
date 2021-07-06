from os import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox = '/Users/Andres/Documents/geckodriver'
driver = webdriver.Firefox(executable_path=firefox)
# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# # ----------------------------------- hacer click ---------------------------------- #
# article_count = driver.find_element_by_css_selector('#articlecount > a')
# # article_count.click()
# # ------------------------------------- buscando por el texto ------------------------------------ #
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
# # ---------------------------------- usando input ---------------------------------- #
# input = driver.find_element_by_name('search')
# input.send_keys('Elsa Jean')
# input.send_keys(Keys.ENTER)
# # driver.quit()

# ---------------------------------------------------------------------------- #
#                                   challenge                                  #
# ---------------------------------------------------------------------------- #
driver.get('http://secure-retreat-92358.herokuapp.com/')
name = driver.find_element_by_name('fName')
name.send_keys('Elsa')


lastName = driver.find_element_by_name('lName')
lastName.send_keys('Jean')

email = driver.find_element_by_name('email')
email.send_keys('Elsita@gmail.com')
email.send_keys(Keys.TAB)
email.send_keys(Keys.ENTER)