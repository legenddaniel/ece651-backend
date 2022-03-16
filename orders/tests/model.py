from django.test import TestCase
from decimal import Decimal

from project.setup_test import AbstractTestSetup


class OrderModelTest(TestCase, AbstractTestSetup):

    # Set up test
    @classmethod
    def setUpTestData(self):
        AbstractTestSetup.setup_user(self, signin=True)
        AbstractTestSetup.setup_products(self)
        AbstractTestSetup.setup_orders(self)

    def test_order(self):
        item = self.orders[0]
        self.assertEqual(str(item), "{}, {}".format(self.user, item.id))
        self.assertEqual(item.user, self.user)
        self.assertEqual(item.status, 'unpaid')
        self.assertEqual(
            item.subtotal, self.products[0].price + self.products[1].price)
        self.assertEqual(item.tax, item.subtotal * Decimal(0.13))
        self.assertEqual(item.total, item.subtotal * Decimal(1.13))

    def test_order_item(self):
        item = self.orders[0].order_items.first()
        self.assertEqual(str(item), str(
            self.orders[0]) + " - " + str(self.products[0]))
        self.assertEqual(item.order, self.orders[0])
        self.assertEqual(item.product, self.products[0])
        self.assertEqual(item.quantity, 1)
        self.assertEqual(item.unit_price, self.products[0].price)
