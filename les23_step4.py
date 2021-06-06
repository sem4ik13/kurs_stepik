from selenium import webdriver
import time
import math

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/alert_accept.html")
	submit_button = browser.find_element_by_css_selector("[type='submit']")
	submit_button.click()
	confirm = browser.switch_to.alert
	confirm.accept()
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	x_element = browser.find_element_by_css_selector("span[id='input_value']")
	x = x_element.text
	y = calc(x)
	input = browser.find_element_by_css_selector("#answer")
	input.send_keys(y)
	submit_button = browser.find_element_by_css_selector("[type='submit']")
	submit_button.click()
finally:
	time.sleep(30)
	browser.quit()