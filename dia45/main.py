from selenium import webdriver

firefox_path = r"C:\Users\plagu\Documents\Development\geckodriver.exe"
driver = webdriver.Firefox(executable_path=firefox_path)
driver.get("https://www.empireonline.com/movies/features/best-movies-2/")

names = driver.find_elements_by_css_selector('div.jsx-3821216435 > h3')
name_list = [ name.text for name in names]
with open('files.txt','w') as datafile:
    datafile.write(str(name_list))
driver.quit()