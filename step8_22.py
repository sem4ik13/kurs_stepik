from selenium import webdriver
import time
import os 

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/file_input.html")
	input1 = browser.find_element_by_name("firstname")
	input1.send_keys("Imya")
	input2 = browser.find_element_by_name("lastname")
	input2.send_keys("Familiya")
	input3 = browser.find_element_by_name("email")
	input3.send_keys("Pochta")
	current_dir = os.path.abspath(os.path.dirname(__file__))
	# получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'file.txt')
	# добавляем к этому пути имя файла 
	element = browser.find_element_by_id("file")
	element.send_keys(file_path)
	submit_button = browser.find_element_by_css_selector("[type='submit']")
	submit_button.click()
finally:
	time.sleep(30)
	browser.quit()