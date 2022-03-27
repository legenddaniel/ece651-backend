from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

@tag('selenium-backend')
@override_settings(ALLOWED_HOSTS=['*'])
class SeleniumTest(TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        self.browser = webdriver.Remote("http://selenium:4444/wd/hub", desired_capabilities=options.to_capabilities())

    def tearDown(self):
        self.browser.quit()

    def test_product_title(self):
        self.browser.get('https://lehshop.xyz/api/products')
        self.assertIn(self.browser.title, 'Products – Django REST framework')
        content = self.browser.find_element_by_class_name('page-header')
        self.assertIn(content.text, 'Products')

