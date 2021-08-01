from typing import Text
import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('lesson', [
	"236895",
	"236896",
	"236897",
	"236898",
	"236899",
	"236903",
	"236904",
	"236905",
	])
class TestParam:
	def test_link_answer(self, browser, lesson):
		answer = math.log(int(time.time() + 0.8))
		link = f"https://stepik.org/lesson/{lesson}/step/1"
		browser.get(link)
		browser.implicitly_wait(10)
		input = browser.find_element_by_css_selector(".textarea")
		input.send_keys(str(answer))
		button = WebDriverWait(browser, 5).until(
			EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
		)
		button.click()
		message = WebDriverWait(browser,5).until(
			EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
		)
		time.sleep(1)
		assert (message.text == "Correct!"), f"{message.text}"


