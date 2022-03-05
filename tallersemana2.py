from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from warnings import filterwarnings
filterwarnings("ignore")

class TestSe(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome(executable_path="./drivers/chromedriver")

	def test_load(self):
		browser = self.browser
        browser.get("https://demo.guru99.com/test/login.html")
        self.driver.find_element(By.ID, "email").send_keys("1")
        self.driver.find_element(By.ID, "passwd").send_keys("1")
        submitButton = browser.find_element_by_css_selector("#SubmitLogin").click()
        sleep(2)
        tbody= browser.find_element_by_css_selector("h3"
        self.driver.find_element(By.ID, "passwd").send_keys("1")
        self.assertIn('Successfully Logged', tbody)
				
		

	def tearDown(self):
		self.browser.quit()


if __name__ == '__main__':
	main()
		
		
		
        
        
        
      
		
