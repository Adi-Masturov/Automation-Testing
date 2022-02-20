import os
import sys
from selenium import webdriver


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    class TrainingPage:
        def __init__(self, driver):
            self.driver = driver
            self.url ='https://techstepacademy.com/training-ground'

        def go(self):
            self.driver.get(self.url)

        def type_into_input(self, text):
            input = self.driver.find_element_by_id('ipt1')
            input.clear()
            input.send_keys(text)
            return None

        def get_input_text(self):
            input = self.driver.find_element_by_id('ipt1')
            elem_text = input.get_attribute('value') 
            return elem_text

        def click_button_1(self):
            button = self.driver.find_element_by_id('b1')
            button.click()
            return None

#Our Test
    from selenium import webdriver

#Test Setup
    browser = webdriver.Chrome()
    test_value = 'it worked'

#Test
    trng_page = TrainingPage(driver=browser)
    trng_page.go()
    trng_page.type_into_input('it worked')
    trng_page.click_button_1()
    txt_from_input = trng_page.get_input_text()
    assert txt_from_input == test_value, "Test Failed"
    print('Test Passed')

