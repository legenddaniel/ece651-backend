from django.test import TestCase, tag, override_settings
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

# @tag('selenium')
@override_settings(ALLOWED_HOSTS=['*'])
class SeleniumTest(TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        self.browser = webdriver.Remote("http://selenium:4444/wd/hub", desired_capabilities=options.to_capabilities())

    def tearDown(self):
        self.browser.quit()

    def test_product_title(self):
        self.browser.get('https://lehshop.xyz/api/recipes')
        self.assertIn(self.browser.title, 'Recipes – Django REST framework')
        content = self.browser.find_element_by_class_name('page-header')
        self.assertIn(content.text, 'Recipes')