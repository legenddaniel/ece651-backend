from rest_framework.test import APITestCase

from project.setup_test import AbstractTestSetup


class CartTest(APITestCase, AbstractTestSetup):
    @classmethod
    def setUpTestData(self):
        AbstractTestSetup.setup_user(self, signin=True)
        AbstractTestSetup.setup_products(self)
        AbstractTestSetup.setup_cart_items(self)

    def test_get_cart(self):
        tests = [
            # Tests that do not require auth first
            {
                'auth': False,
                'assertions': [
                    # Should not valid to unauthed user
                    lambda res: self.assertEqual(
                        res.status_code, 401),
                ]
            },
            {
                'auth': True,
                'assertions': [
                    # Should contain some fields
                    lambda res: [self.assertIn(field, res.data[0])
                                 for field in ('id', 'product', 'quantity')],
                    lambda res: [self.assertIn(field, res.data[0]['product']) for field in (
                        'id', 'name', 'price', 'stock', 'image_url')],

                    # Should belong to current user
                    lambda res: self.assertEqual(
                        res.data[0]['user'], self.user.id),
                ]
            },
        ]

        for test in tests:
            if test['auth']:
                self.client.credentials(
                    HTTP_AUTHORIZATION='Token ' + self.token)
            else:
                self.client.credentials()

            res = self.client.get('/api/cart/')
            for assertion in test['assertions']:
                assertion(res)

    def test_create_cart(self):
        tests = [
            # Tests that do not require auth first
            {
                'auth': False,
                'data': {
                    "product_id": 1,
                    "quantity": 1
                },
                'assertions': [
                    # Should not valid to unauthed user
                    lambda res: self.assertEqual(res.status_code, 401),
                ]
            },
            {
                'auth': True,
                'data': {
                    "product_id": 123131,
                    "quantity": 1
                },
                'assertions': [
                    # Should not add a invalid product to cart
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
            {
                'auth': True,
                'data': {
                    "product_id": 1,
                    "quantity": 1
                },
                'assertions': [
                    # We have product 1 in cart, so should update the quantity
                    lambda res: self.assertEqual(len(res.data), 2),
                    lambda res: self.assertEqual(
                        res.data[0]['quantity'], self.cart_items[0]['quantity'] + 1),
                ]
            },
            {
                'auth': True,
                'data': {
                    "product_id": 3,
                    "quantity": 1
                },
                'assertions': [
                    # Add a new product
                    lambda res: self.assertEqual(len(res.data), 3),
                    lambda res: self.assertEqual(res.data[2]['quantity'], 1),
                ]
            },
            {
                'auth': True,
                'data': {
                    "product": 3,
                    "quantity": 1
                },
                'assertions': [
                    # Wrong field
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
        ]

        for test in tests:
            if test['auth']:
                self.client.credentials(
                    HTTP_AUTHORIZATION='Token ' + self.token)
            else:
                self.client.credentials()

            res = self.client.post('/api/cart/', test['data'])
            for assertion in test['assertions']:
                assertion(res)

    def test_update_cart(self):
        tests = [
            # Tests that do not require auth first
            {
                'auth': False,
                'item_id': 1,
                'data': {
                    "quantity": 1
                },
                'assertions': [
                    # Should not valid to unauthed user
                    lambda res: self.assertEqual(res.status_code, 401),
                ]
            },
            {
                'auth': True,
                'item_id': 1,
                'data': {
                    "quantity": 1
                },
                'assertions': [
                    # Change first item quantity to 1
                    lambda res: self.assertEqual(res.data[0]['quantity'], 1),
                ]
            },
            {
                'auth': True,
                'item_id': 1312312,
                'data': {
                    "quantity": 1
                },
                'assertions': [
                    # Invalid item id
                    lambda res: self.assertEqual(res.status_code, 404),
                ]
            },
            {
                'auth': True,
                'item_id': 1,
                'data': {
                    "quantity": 0
                },
                'assertions': [
                    # Remove first item
                    lambda res: self.assertEqual(len(res.data), 1),
                ]
            },
            {
                'auth': True,
                'item_id': 1,
                'data': {
                    "quantit": 5
                },
                'assertions': [
                    # Wrong field
                    lambda res: self.assertGreaterEqual(res.status_code, 400),
                ]
            },
        ]

        for test in tests:
            if test['auth']:
                self.client.credentials(
                    HTTP_AUTHORIZATION='Token ' + self.token)
            else:
                self.client.credentials()

            res = self.client.patch('/api/cart/%d/' %
                                    test['item_id'], test['data'])
            for assertion in test['assertions']:
                assertion(res)

    def test_clear_cart(self):
        tests = [
            # Tests that do not require auth first
            {
                'auth': False,
                'assertions': [
                    # Should not valid to unauthed user
                    lambda res: self.assertEqual(res.status_code, 401),
                ]
            },
            {
                'auth': True,
                'assertions': [
                    # Should clear cart
                    lambda res: self.assertEqual(res.status_code, 204),
                ]
            },
        ]

        for test in tests:
            if test['auth']:
                self.client.credentials(
                    HTTP_AUTHORIZATION='Token ' + self.token)
            else:
                self.client.credentials()

            res = self.client.delete('/api/cart/')
            for assertion in test['assertions']:
                assertion(res)
