from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def calc(x,y):
   	  return str(int(x) + int(y))

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/selects2.html")
	num_1 = browser.find_element_by_css_selector("span[id='num1']")
	x = num_1.text
	num_2 = browser.find_element_by_css_selector("span[id='num2']")
	y = num_2.text
	z = calc(x,y)
	print(z)
	select_s = Select(browser.find_element_by_xpath("//select[@class='custom-select']"))
	select_s.select_by_value(z)
	submit_button = browser.find_element_by_css_selector("[type='submit']")
	submit_button.click()
finally:
	time.sleep(30)
	browser.quit()