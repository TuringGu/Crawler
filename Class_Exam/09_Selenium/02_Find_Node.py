from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')


# Find single node
# input_first = browser.find_element_by_id('q')
input_first = browser.find_element(By.ID, 'q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')

print(input_first)
print(input_second)
print(input_third)
# browser.close()


# Find mutiple nodes
# lis = browser.find_elements_by_css_selector('.service-bd li')
lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
print(lis)
browser.close()