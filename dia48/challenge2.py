from selenium import webdriver

firefox = '/Users/Andres/Documents/geckodriver'
driver = webdriver.Firefox(executable_path=firefox)
driver.get('https://en.wikipedia.org/wiki/Main_Page')
number = driver.find_element_by_css_selector('#articlecount > a')
print(number.text)
driver.quit()

