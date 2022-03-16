from django.test import TestCase

from project.setup_test import AbstractTestSetup


class CartModelTest(TestCase, AbstractTestSetup):

    # Set up test
    @classmethod
    def setUpTestData(self):
        AbstractTestSetup.setup_user(self, signin=True)
        AbstractTestSetup.setup_products(self)
        AbstractTestSetup.setup_cart_items(self)

    def test_cart(self):
        item = self.cart_items[0]
        self.assertEqual(str(item), "{}, {}".format(
            self.user, self.products[0]))
        self.assertEqual(item.user, self.user)
        self.assertEqual(item.product, self.products[0])
        self.assertEqual(item.quantity, 5)
