from project.setup_test import AbstractTestSetup
from django.test import LiveServerTestCase, override_settings, tag
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from django.conf import settings
import os
from time import sleep

os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = '0.0.0.0:8001'


@tag('selenium-system')
@override_settings(ALLOWED_HOSTS=['*'])
class SystemTestOrder2(LiveServerTestCase, AbstractTestSetup):
    @classmethod
    def setUpClass(cls):
        cls.host = "0.0.0.0"
        cls.port = 8001
        super(SystemTestOrder2, cls).setUpClass()
        settings.DEBUG = True
        AbstractTestSetup.setup_webdriver(cls)
        AbstractTestSetup.setup_products(cls)
        AbstractTestSetup.setup_recipe(cls)

    def tearDown(self):
        self.browser.quit()

    def test_recipe_cart_order(self):
        print("\nStarting system test for: user signup => user login => search for a recipe => add products in recipe to cart => add address => place order")
        EMAIL = 'test@test.com'
        USERNAME = 'test'
        PASSWORD = '12345678'

        '''
        Search recipe and add products to cart, then create order and place
        '''

        from users.models import User
        from knox.models import AuthToken
        from carts.models import CartItem
        from orders.models import OrderItem

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
        login = form.find_element(by=By.CSS_SELECTOR, value='.succ > a.login')
        login.click()
        form = self.browser.find_element(by=By.CSS_SELECTOR, value='form')
        form.find_element(by=By.ID, value='email').send_keys(EMAIL)
        form.find_element(by=By.ID, value='password').send_keys(PASSWORD)
        form.find_element(by=By.CSS_SELECTOR,
                          value='button.btn[type=submit]').click()
        WebDriverWait(self.browser, 5).until(
            lambda x: self.browser.find_element_by_xpath("//a[@class='nav-link pr-0 userDetail']"))
        self.assertEqual(len(AuthToken.objects.filter(user=user)), 1)

        # Search recipe and add to cart
        self.browser.find_element(by=By.CLASS_NAME, value='recipelist').click()
        sleep(1)
        self.browser.find_element(
            by=By.CSS_SELECTOR, value='app-recipe-list > .container > .row > div:first-of-type > app-recipe > a').click()
        sleep(1)
        self.browser.find_element(by=By.ID, value='buttonAdd').click()
        sleep(1)
        self.assertEqual(CartItem.objects.get(
            product_id=self.products[0].id).quantity, 1)

        # Change Information (Add address)
        self.browser.find_element_by_xpath(
            "//a[@class='nav-link pr-0 userDetail']").click()
        WebDriverWait(self.browser, 5).until(
            lambda x: self.browser.find_element_by_class_name("shoppingCart"))
        self.browser.find_element_by_class_name("shoppingCart").click()
        WebDriverWait(self.browser, 5).until(
            lambda x: self.browser.find_element_by_id("checkout-btn"))
        self.browser.find_element(by=By.ID, value='checkout-btn').click()
        WebDriverWait(self.browser, 5).until(
            lambda x: self.browser.find_element(
                by=By.CSS_SELECTOR, value='app-shopping-cart-detail > .container > div.row:last-of-type .row > div:nth-last-of-type(1) > .btn'))
        self.browser.find_element(
            by=By.CSS_SELECTOR,
            value='app-shopping-cart-detail > .container > div.row:last-of-type .row > div:nth-of-type(1) > .btn').click()
        WebDriverWait(self.browser, 5).until(
            lambda x: self.browser.find_element(by=By.ID, value='change-btn'))
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

        # Create order
        self.browser.find_element_by_class_name("shoppingCart").click()
        WebDriverWait(self.browser, 5).until(
            lambda x: self.browser.find_element_by_id("checkout-btn"))
        self.browser.find_element(by=By.ID, value='checkout-btn').click()
        WebDriverWait(self.browser, 5).until(
            lambda x: self.browser.find_element(
                by=By.CSS_SELECTOR, value='app-shopping-cart-detail > .container > div.row:last-of-type .row > div:last-of-type > .btn'))
        self.browser.find_element(
            by=By.CSS_SELECTOR, value='app-shopping-cart-detail > .container > div.row:last-of-type .row > div:last-of-type > .btn').click()
        WebDriverWait(self.browser, 5).until(
            lambda x: alert_is_present())
        alert_obj = self.browser.switch_to.alert
        alert_obj.accept()
        # navigate to the order page
        self.browser.find_element_by_xpath(
            "//a[@class='nav-link pr-0 userDetail']").click()
        WebDriverWait(self.browser, 5).until(
            lambda x: self.browser.find_element_by_class_name("orderList"))
        self.browser.find_element_by_class_name("orderList").click()
        sleep(1)
        item = OrderItem.objects.get(product_id=self.products[0].id)
        self.assertEqual(item.quantity, 1)
