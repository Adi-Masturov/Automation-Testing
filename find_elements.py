from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/training-ground')

input2_css_locator = "input[id='ipt2']"
button4_xpath_locator = "//button[@id='b4']"

input1 = browser.find_element('id','ipt1')

input1.send_keys("Test_text")

input_elementer = browser.find_element_by_css_selctor('input[id="ipt1"]')
input_elementer.find_element('input[id="ipt1"]')


