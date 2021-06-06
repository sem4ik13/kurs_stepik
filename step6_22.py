from selenium import webdriver
import time
import math
	
try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/execute_script.html")
	def calc(x):
		  return str(math.log(abs(12*math.sin(int(x)))))
	x_element = browser.find_element_by_css_selector("span[id='input_value']")
	x = x_element.text
	y = calc(x)
	input = browser.find_element_by_css_selector("#answer")
	input.send_keys(y)
	option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
	browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
	option1.click()
	option1 = browser.find_element_by_css_selector("[value='robots']")
	browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
	option1.click()
	
finally:
	time.sleep(10)
	browser.quit()