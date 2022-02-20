import os
import sys
from selenium import webdriver
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    print_hi('PyCharm')
    print(os.path.dirname(sys.executable))

    browser = webdriver.Chrome()
    browser.get('https://techstepacademy.com/training-ground')
    print(browser)



