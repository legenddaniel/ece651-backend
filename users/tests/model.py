from django.test import TestCase

from project.setup_test import AbstractTestSetup

'''
class UserModelTest(TestCase, AbstractTestSetup):

    # Set up test
    @classmethod
    def setUpTestData(self):
        AbstractTestSetup.setup_superuser(self)
        AbstractTestSetup.setup_user(self, signin=True)
        AbstractTestSetup.setup_ship_add(self)
        AbstractTestSetup.setup_products(self)
        AbstractTestSetup.setup_orders(self)
        AbstractTestSetup.setup_cart_items(self)

    def test_superuser(self):
        item = self.superuser
        self.assertEqual(str(item), self.superuser.email)
        self.assertEqual(item.email, 'admin@test.com')
        self.assertNotEqual(item.password, '12345678')
        self.assertEqual(item.is_superuser, True)

    def test_user(self):
        item = self.user
        self.assertEqual(str(item), self.user.email)
        self.assertEqual(item.email, 'test@test.com')
        self.assertNotEqual(item.password, '12345678')
        self.assertEqual(item.is_superuser, False)

    def test_shipping_address(self):
        item = self.shipping_address
        self.assertEqual(str(item), self.user.username + ' address')
        self.assertEqual(item.user, self.user)
        self.assertEqual(item.full_name, 'aaa')
        self.assertEqual(item.phone_number, '1234567890')
        self.assertEqual(item.address, 'First St')
        self.assertEqual(item.province, 'ON')'''
