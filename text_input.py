from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.google.com")
search_input = browser.find_element_by_name("q")
search_input.send_keys("selenium")
search_input.send_keys(Keys.ENTER)
assert("https://www.google.com/search" in browser.current_url)