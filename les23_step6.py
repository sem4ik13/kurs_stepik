from selenium import webdriver
import time
import math

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/redirect_accept.html")
	submit_button1 = browser.find_element_by_css_selector("[type='submit']")
	submit_button1.click()
	first_window = browser.window_handles[0]
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	x_element = browser.find_element_by_css_selector("span[id='input_value']")
	x = x_element.text
	y = calc(x)
	input = browser.find_element_by_css_selector("#answer")
	input.send_keys(y)
	submit_button2 = browser.find_element_by_css_selector("[type='submit']")
	submit_button2.click()
finally:
	time.sleep(3)
	browser.quit()