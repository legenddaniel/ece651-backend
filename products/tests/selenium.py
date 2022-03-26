from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SeleniumTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME)

    def tearDown(self):
        self.browser.quit()

    def test_site_title(self):
        self.browser.get('https://lehstore.web.app/')
        print(self.browser.title)
        self.assertIn(self.browser.title, 'Lehstore')
