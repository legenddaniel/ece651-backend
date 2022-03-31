from django.test import TestCase, tag, override_settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import socket
from django.conf import settings
from project.setup_test import AbstractTestSetup

os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS']='0.0.0.0:8001'

@tag('selenium-backend')
@override_settings(ALLOWED_HOSTS=['*'])
class SeleniumTest(StaticLiveServerTestCase):
    live_server_url = 'http://{}:8001'.format(socket.gethostbyname(socket.gethostname()))
    @classmethod
    def setUpClass(cls):
        cls.host = "0.0.0.0"  # or ip
        cls.port = 8001
        super(SeleniumTest, cls).setUpClass()
        settings.DEBUG = True
        options = webdriver.ChromeOptions()
        options.add_argument('--allow-insecure-localhost')
        options.add_argument('--ignore-certificate-errors')
        capabilities = options.to_capabilities()
        capabilities['acceptInsecureCerts'] = True
        cls.browser = webdriver.Remote(command_executor="http://selenium:4444/wd/hub", desired_capabilities=capabilities)
        AbstractTestSetup.setup_products(cls)

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    # def test_backend_product_title(self):
    #     print(self.live_server_url)
    #     self.browser.get(self.live_server_url+"/api/products/")
    #     self.assertIn(self.browser.title, 'Products – Django REST framework')
    #     content = self.browser.find_element_by_class_name('page-header')
    #     self.assertIn(content.text, 'Products')

    def test_products(self):
        print(self.live_server_url)
        # self.browser.get(self.live_server_url+'/api/products/?name=test1/')
        self.browser.get('http://lehstore')
        print(self.browser.page_source)

