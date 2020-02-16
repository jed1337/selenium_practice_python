from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()

# A page that uses JS to implement drag and drop
browser.get("https://jqueryui.com/resources/demos/sortable/connect-lists.html")

ul = browser.find_element_by_xpath("//ul[@id='sortable1']")
ul_highlight = browser.find_element_by_xpath("//ul[@id='sortable2']")

# The element contains two classes
# We use contains() to match on only one of the classes
item1 = browser.find_element_by_xpath("//li[contains(@class,'ui-state-default') and contains(text(), 'Item 1')]")
item1_highlight = browser.find_element_by_xpath("//li[contains(@class,'ui-state-highlight') and contains(text(), 'Item 1')]")

ActionChains(browser).drag_and_drop(item1, ul_highlight).perform()
ActionChains(browser).drag_and_drop(item1_highlight, ul).perform()