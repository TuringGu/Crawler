from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
url = 'file:///D:/Develop/Crawler/Class_Exam/09_Selenium/Drop_Demo.html'
browser.get(url)
# browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()

