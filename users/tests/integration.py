import socket
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from django.test import TestCase, LiveServerTestCase, override_settings, tag
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings

@tag('selenium')
@override_settings(ALLOWED_HOSTS=['*'])
class UserIntegrationTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.host = socket.gethostbyname(socket.gethostname())
        print('setup')
        cls.selenium = webdriver.Remote(
            command_executor='http://localhost:4444',
            desired_capabilities=DesiredCapabilities.CHROME,
        )
        print('connected')
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
        print('quit')

    def test_test(self):
        print('test')
        self.selenium.get('https://www.selenium.dev/')
        print(self.selenium.find_element_by_id('td-cover-block-0'))

