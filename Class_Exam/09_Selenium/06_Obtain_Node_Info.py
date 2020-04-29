from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://dynamic2.scrape.cuiqingcai.com/'
browser.get(url)
logo = browser.find_element_by_class_name('logo-image')
inputs = browser.find_element_by_class_name('logo-title')

print(logo)
print(logo.get_attribute('src'))    # Get Attribute
print('')
print(inputs)
print(inputs.text)   # Get input text
print(inputs.id)
print(inputs.location)
print(inputs.tag_name)
print(inputs.size)
