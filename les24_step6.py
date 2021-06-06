from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"),'$100')
	)
browser.find_element_by_id("book").click()

def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_css_selector("span[id='input_value']")
x = x_element.text
y = calc(x)
input = browser.find_element_by_css_selector("#answer")
input.send_keys(y)
submit_button2 = browser.find_element_by_css_selector("[type='submit']")
submit_button2.click()
time.sleep(5)
browser.quit()