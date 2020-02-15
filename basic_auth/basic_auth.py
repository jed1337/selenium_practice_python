from selenium import webdriver

# Assume that chromedriver.exe is in the path
browser = webdriver.Chrome()

# http://<username>:<password>@<webpage with basic authentication>
browser.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')

footer = browser.find_element_by_id('page-footer')

assert(footer.text == 'Powered by Elemental Selenium')

browser.close()