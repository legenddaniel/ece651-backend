from project.setup_test import AbstractTestSetup
from django.test import TestCase, LiveServerTestCase, override_settings, tag
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from django.conf import settings
import os
from time import sleep
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS']='0.0.0.0:8001'
@tag('selenium-system')
@override_settings(ALLOWED_HOSTS=['*'])
class SystemTestUser(LiveServerTestCase, AbstractTestSetup):
    @classmethod
    def setUpClass(cls):
        cls.host = "0.0.0.0"
        cls.port = 8001
        super(SystemTestUser, cls).setUpClass()
        settings.DEBUG = True
        AbstractTestSetup.setup_webdriver(cls)
        AbstractTestSetup.setup_products(cls)

    def tearDown(self):
        self.browser.quit()

    def test_signup_signin_address(self):
        print("\nStarting system test for: user signup => user login => add shipping address => change shipping address")
        EMAIL = 'test@test.com'
        USERNAME = 'test'
        PASSWORD = '12345678'
        '''
        Sign up, then sign in, then add/modify the shipping address
        '''

        from users.models import User
        from knox.models import AuthToken

        # Sign up
        self.assertEqual(len(User.objects.filter(email=EMAIL)), 0)
        self.browser.get(self.fe)
        loginbtn = self.browser.find_element_by_css_selector("a#fontSignup")
        loginbtn.click()
        form = self.browser.find_element(by=By.CSS_SELECTOR, value='form')
        form.find_element(by=By.ID, value='email').send_keys(EMAIL)
        form.find_element(by=By.ID, value='name').send_keys(USERNAME)
        form.find_element(by=By.ID, value='password').send_keys(PASSWORD)
        form.find_element(by=By.CSS_SELECTOR,
                          value='button.btn[type=submit]').click()
        WebDriverWait(self.browser, 5).until(
            lambda x: form.find_element(by=By.CSS_SELECTOR, value='.succ > a.login'))
        user = User.objects.get(email=EMAIL)
        self.assertEqual(user.username, USERNAME)

        # Log in
        self.browser.get(self.fe)
        loginbtn = self.browser.find_element_by_css_selector("a#fontLogin")
        loginbtn.click()
        form = self.browser.find_element(by=By.CSS_SELECTOR, value='form')
        form.find_element(by=By.ID, value='email').send_keys(EMAIL)
        form.find_element(by=By.ID, value='password').send_keys(PASSWORD)
        form.find_element(by=By.CSS_SELECTOR,
                          value='button.btn[type=submit]').click()
        WebDriverWait(self.browser, 5).until(
            lambda x: self.browser.find_element_by_xpath("//a[@class='nav-link pr-0 userDetail']"))
        self.assertEqual(len(AuthToken.objects.filter(user=user)), 1)
        self.assertEqual(len(AuthToken.objects.filter(user=user)), 1)

        # Add shipping address
        self.browser.find_element_by_xpath("//a[@class='nav-link pr-0 userDetail']").click()
        self.browser.find_element(by=By.ID, value='change-btn').click()
        self.browser.find_element(
            by=By.ID, value='floatingcardID').send_keys('1111222211112222')
        self.browser.find_element(
            by=By.ID, value='floatingAddress').send_keys('1 John St')
        self.browser.find_element(
            by=By.ID, value='floatingSelect').send_keys('ON')
        self.browser.find_element(
            by=By.ID, value='floatingPhoneNum').send_keys('1234567890')
        self.browser.find_element(
            by=By.ID, value='floatingPostalCode').send_keys('M2W2W2')
        self.browser.find_element(by=By.ID, value='submit-btn').click()
        WebDriverWait(self.browser, 5).until(
            lambda x: x.find_element(by=By.ID, value='change-btn'))

        user = User.objects.get(email=EMAIL)
        self.assertEqual(user.credit_card, '1111222211112222')
        self.assertEqual(user.shipping_address.phone_number, '1234567890')

        # # Change shipping address
        self.browser.find_element(by=By.ID, value='change-btn').click()
        self.browser.find_element(
            by=By.ID, value='floatingcardID').clear()
        self.browser.find_element(
            by=By.ID, value='floatingcardID').send_keys('1111222211112223')
        self.browser.find_element(
            by=By.ID, value='floatingAddress').clear()
        self.browser.find_element(
            by=By.ID, value='floatingAddress').send_keys('1 John St')
        self.browser.find_element(
            by=By.ID, value='floatingSelect').send_keys('ON')
        self.browser.find_element(
            by=By.ID, value='floatingPhoneNum').clear()
        self.browser.find_element(
            by=By.ID, value='floatingPhoneNum').send_keys('1234567891')
        self.browser.find_element(
            by=By.ID, value='floatingPostalCode').clear()
        self.browser.find_element(
            by=By.ID, value='floatingPostalCode').send_keys('M2W2W2')
        self.browser.find_element(by=By.ID, value='submit-btn').click()
        WebDriverWait(self.browser, 5).until(
            lambda x: x.find_element(by=By.ID, value='change-btn'))
        user = User.objects.get(email=EMAIL)
        self.assertEqual(user.credit_card, '1111222211112223')
        self.assertEqual(user.shipping_address.phone_number, '1234567891')

    # def test_search_cart_order(self):
    #     SEARCH = 'te'
    #     EMAIL = 'test@test.com'
    #     PASSWORD = '12345678'
    #
    #     '''
    #     Search product and add it to cart, then create order and place
    #     '''
    #
    #     from carts.models import CartItem
    #     from orders.models import OrderItem
    #
    #     # Log in
    #     self.browser.get(self.fe + '/login')
    #     form = self.browser.find_element(by=By.CSS_SELECTOR, value='form')
    #     form.find_element(by=By.ID, value='email').send_keys(EMAIL)
    #     form.find_element(by=By.ID, value='password').send_keys(PASSWORD)
    #     form.find_element(by=By.CSS_SELECTOR,
    #                       value='button.btn[type=submit]').click()
    #     WebDriverWait(self.browser, 5).until(
    #         lambda x: x.current_url == self.fe)
    #
    #     # Search product
    #     self.browser.get(self.fe)
    #     searchbar = self.browser.find_element(
    #         by=By.CSS_SELECTOR, value='.navbar-nav+div')
    #     searchbar.find_element(by=By.TAG_NAME, value='input').send_keys(SEARCH)
    #     searchbar.find_element(by=By.TAG_NAME, value='a').click()
    #     WebDriverWait(self.browser, 5).until(
    #         lambda x: x.current_url == self.fe + '/search/' + SEARCH)
    #
    #     list = self.browser.find_elements(by=By.CSS_SELECTOR, value='app-search > .container > .row:last-of-type > div')
    #     self.assertEqual(len(list), len(self.products))
    #
    #     # Add to cart
    #     list[0].find_element(by=By.CSS_SELECTOR, value='app-product-item > a').click()
    #     WebDriverWait(self.browser, 5).until(
    #         lambda x: x.current_url == self.fe + '/productdetail/1')
    #     self.browser.find_element(
    #         by=By.CSS_SELECTOR, value='app-product-item-detail ngx-number-spinner+button.btn').click()
    #     WebDriverWait(self.browser, 5)
    #
    #     self.assertEqual(CartItem.objects.get(product_id=1).quantity, 1)
    #
    #     # Create order
    #     self.browser.get(self.fe + '/shoppingcartDetail')
    #     self.browser.find_element(by=By.ID, value='checkout-btn').click()
    #     self.browser.find_element(
    #         by=By.CSS_SELECTOR, value='app-shopping-cart-detail > .container > div.row:last-of-type .row > div:last-of-type > .btn').click()
    #
    #     WebDriverWait(self.browser, 5).until(
    #         lambda x: alert_is_present())
    #
    #     item = OrderItem.objects.get(product_id=1)
    #     self.assertEqual(item.quantity, 1)
    #     self.assertEqual(item.order.id, 1)
