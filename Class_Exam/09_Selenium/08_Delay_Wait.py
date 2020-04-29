from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Implicitly wait
browser1 = webdriver.Chrome()
browser1.implicitly_wait(10) # Wait
browser1.get('https://dynamic2.scrape.cuiqingcai.com/')
input1 = browser1.find_element_by_class_name('logo-image')
print(input1)


# Explicity wait
browser2 = webdriver.Chrome()
browser2.get('https://www.taobao.com/')
wait = WebDriverWait(browser2, 10)   # Wait
input2 = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input2)
print(button)
