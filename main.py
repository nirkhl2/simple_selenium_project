import time
from selenium import webdriver

chrome_driver = webdriver.Chrome(executable_path=r'C:\\Users\\nkahila\\Desktop\\Nir\\DevOps\\Course\\programs\\chromedriver_win32\\chromedriver.exe')
chrome_driver.get('http://www.google.com/')
time.sleep(5)  # Let the user actually see something!
search_box = chrome_driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)  # Let the user actually see something!
chrome_driver.quit()
