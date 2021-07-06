from selenium import webdriver
import time

timeout = time.time() + 60
firefox = '/Users/Andres/Documents/geckodriver'
driver = webdriver.Firefox(executable_path=firefox)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
def click_cookie():
    cookie = driver.find_element_by_id('cookie')
    cookie.click()
def buy_cookie():
    hands = 0;
    cursor = driver.find_element_by_id('buyCursor')
    cursor.click()
    hands += 1
    return hands

while time.time() < timeout:
    score = driver.find_element_by_id('money')
    click_cookie()

    if int(score.text) >= 15:
         a = buy_cookie()
         print(a)
driver.quit()