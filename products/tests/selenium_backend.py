from django.test import TestCase, tag, override_settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import socket
from django.conf import settings

os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS']='0.0.0.0:8000'

@tag('selenium-backend')
@override_settings(ALLOWED_HOSTS=['*'])
class SeleniumTest(StaticLiveServerTestCase):
    print(socket.gethostname())
    print(socket.gethostbyname(socket.gethostname()))
    live_server_url = 'http://{}:8000'.format(socket.gethostbyname(socket.gethostname()))

    def setUp(self):
        settings.DEBUG = True
        options = webdriver.ChromeOptions()
        options.add_argument('--allow-insecure-localhost')
        options.add_argument('--ignore-certificate-errors')
        capabilities = options.to_capabilities()
        capabilities['acceptInsecureCerts'] = True
        self.browser = webdriver.Remote(command_executor="http://selenium:4444/wd/hub", desired_capabilities=capabilities)

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def test_backend_product_title(self):
        self.browser.get(self.live_server_url+"/api/products/")
        self.assertIn(self.browser.title, 'Products – Django REST framework')
        content = self.browser.find_element_by_class_name('page-header')
        self.assertIn(content.text, 'Products')

    def test_lehstore_product_price(self):
        self.browser.get("http://lehstore")
        price_element = self.browser.find_element_by_class_name('price')
        price = price_element.text
        self.assertEqual(price, '$12.69')
