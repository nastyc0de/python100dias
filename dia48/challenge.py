from selenium import webdriver

firefox_path = '/Users/Andres/Documents/geckodriver'
driver = webdriver.Firefox(executable_path=firefox_path)
driver.get('https://www.python.org/')
theEvents = {}
time_events = driver.find_elements_by_css_selector('.event-widget > div > ul > li > time')
title_events = driver.find_elements_by_css_selector('.event-widget > div > ul > li > a')
for n in range(len(time_events)):
    theEvents[n] = {
        'time': time_events[n].text,
        'name': title_events[n].text
    }
print(theEvents)
driver.quit()