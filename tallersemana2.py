from pip import main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest
from warnings import filterwarnings
import undetected_chromedriver as uc
filterwarnings("ignore")

class TestSe(unittest.TestCase):

	def setUp(self):
		 
		self.browser = webdriver.ChromeOptions()
		
		 

	def test_load(self):
		self.browser.headless = True
		brow = uc.Chrome()
		brow.get("https://demo.guru99.com/test/login.html")
		self.browser.find_element(By.ID, "email").send_keys("1")
		self.browser.find_element(By.ID, "passwd").send_keys("1")
		submitButton = browser.find_element_by_css_selector("#SubmitLogin").click()
		sleep(2)
		tbody= browser.find_element_by_css_selector("h3").text
		self.assertIn('Successfully Logged', tbody)
		

	def tearDown(self):
		self.browser.quit()


if __name__ == '__main__':
	main()
	
