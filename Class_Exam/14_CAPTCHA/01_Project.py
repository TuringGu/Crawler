import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Plateform.chaojiying import Chaojiying


SCREEN_FACTOR = 1.5         # Screenshot factor
MAX_TIMEOUT = 10       # Verify wait time
USERNAME = 'admin'
PASSWORD = 'admin'
CHAOJIYING_USERNAME = ''
CHAOJIYING_PASSWORD = ''
CRACK_URL = 'https://captcha3.scrape.cuiqingcai.com/'
CHAOJIYING_SOFT_ID = 905216 # Generate https://www.chaojiying.com/user/mysoft/
CHAOJIYING_KIND = 9102      # Generate https://www.chaojiying.com/price.html
        

if not CHAOJIYING_USERNAME or not CHAOJIYING_PASSWORD:
    print('Please input username & password')
    exit(0)


class CrackCaptcha():
    # Init
    def __init__(self):
        self.url = CRACK_URL
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 100)
        self.username = USERNAME
        self.password = PASSWORD
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)

    # Get verification code
    def open(self):
        # Open a browser & input username, password
        self.browser.get(self.url)
        username = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
        password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
        username.send_keys(self.username)
        password.send_keys(self.password)

    # Get initial verify button
    def get_captcha_button(self):
        button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="button"]')))
        return button

    # Get verification image element
    def get_captcha_element(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.geetest_item_img')))
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_holder')))
        print('Succeed: Got verification element node!')
        return element

    # Get verification image position
    def get_captcha_position(self):
        element = self.get_captcha_element()
        time.sleep(2)
        location = element.location
        size = element.size
        print('Size', size) # test
        print('location', location) # test
        top = location['y']
        bottom = location['y'] + size['height']
        left = location['x']
        right = location['x'] + size['width']
        print('Get_captcha_position', top, bottom, left, right) # test
        return (top, bottom, left, right)

    # Adjust the screenshot factor
    def adjust_screenshot(self):
        adjust_top, adjust_bottom, adjust_left, adjust_right = self.get_captcha_position()
        adjust_top = adjust_top * SCREEN_FACTOR
        adjust_bottom = adjust_bottom * SCREEN_FACTOR
        adjust_left = adjust_left * SCREEN_FACTOR
        adjust_right = adjust_right * SCREEN_FACTOR
        return (adjust_top, adjust_bottom, adjust_left, adjust_right)

    # Get web page screenshot
    def get_screenshot(self):
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        screenshot.save('screenshot.png')
        return screenshot

    # Get verafication image screenshot
    def get_captcha_image(self, name='captcha.png'):
        # top, bottom, left, right = self.get_captcha_position()
        top, bottom, left, right = self.adjust_screenshot()
        print('Verification image position', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    # Parse recognition result
    def get_points(self, captcha_result):
        groups = captcha_result.get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')] for group in groups]
        return locations

    # Click verification image
    def touch_click_words(self, locations):
        for location in locations:
            # Adjust click position
            location[0] = location[0] / SCREEN_FACTOR     
            location[1] = location[1] / SCREEN_FACTOR        
             
            ActionChains(self.browser).move_to_element_with_offset(self.get_captcha_element(), location[0], location[1]).click().perform()
            print("Touch location:", location[0], location[1])
            time.sleep(1)

    # Crack
    def crack(self):
        self.open()
        # Click button to login
        button = self.get_captcha_button()
        button.click()

        # Obtain verification image
        image = self.get_captcha_image()
        bytes_array = BytesIO()
        image.save(bytes_array, format='PNG')

        # Recognize verification image
        result = self.chaojiying.post_pic(bytes_array.getvalue(), CHAOJIYING_KIND)
        print(result)
        locations = self.get_points(result)
        self.touch_click_words(locations)

        # Click verify button
        button_verify = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_commit_tip')))
        button_verify.click()

        # Judge weather succeed or not
        success = WebDriverWait(self.wait, MAX_TIMEOUT).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), '登录成功'))
        # success = WebDriverWait(self.wait, MAX_TIMEOUT).until(lambda driver: driver.find_element_by_id("someId"))
        print(success)

        # When failure, retry
        if not success:
            print('Failure!')
            self.report_error(self, 'captcha.png')
            # self.crack()
            time.sleep(10)
            self.browser.close()


if __name__ == '__main__':
    crack = CrackCaptcha()
    crack.crack()
    