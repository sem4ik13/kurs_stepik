from typing import Text
from selenium import webdriver
import time
import math
	
def calc(x):
   	  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/get_attribute.html")
	treasure_check = browser.find_element_by_css_selector("img[id='treasure']")
	treasure_attr = treasure_check.get_attribute("valuex")
	x = treasure_attr
	y = calc(x)
	input = browser.find_element_by_css_selector("#answer")
	input.send_keys(y)
	option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
	option1.click()
	option1 = browser.find_element_by_css_selector("[value='robots']")
	option1.click()
	submit_button = browser.find_element_by_css_selector("[type='submit']")
	submit_button.click()
finally:
	time.sleep(30)
	browser.quit()