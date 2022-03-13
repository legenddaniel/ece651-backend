from rest_framework.test import APITestCase

from project.setup_test import AbstractTestSetup


class UserTest(APITestCase, AbstractTestSetup):
    @classmethod
    def setUpTestData(self):
        AbstractTestSetup.setup_user(self, signin=True)
        AbstractTestSetup.setup_ship_add(self)
        AbstractTestSetup.setup_products(self)
        AbstractTestSetup.setup_orders(self)
        AbstractTestSetup.setup_cart_items(self)

    def test_get_user(self):
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
                    lambda res: [self.assertIn(field, res.data)
                                 for field in ('id', 'orders', 'cart_items', 'shipping_address', 'username', 'email', 'credit_card')],

                    # Should not contain password
                    lambda res: self.assertNotIn('password', res.data),

                    # Should contain order item details
                    lambda res: [self.assertIn(field, res.data['orders'][0])
                                 for field in ('id', 'order_items', 'status', 'user')],

                    # Should contain cart item details
                    lambda res: [self.assertIn(field, res.data['cart_items'][0])
                                 for field in ('id', 'quantity', 'product')],
                ]
            },
        ]

        for test in tests:
            if test['auth']:
                self.client.credentials(
                    HTTP_AUTHORIZATION='Token ' + self.token)
            else:
                self.client.credentials()

            res = self.client.get('/api/users/')
            for assertion in test['assertions']:
                assertion(res)

    def test_update_user(self):
        tests = [
            # Tests that do not require auth first
            {
                'auth': False,
                'data': {
                    "username": '1'
                },
                'assertions': [
                    # Should not valid to unauthed user
                    lambda res: self.assertEqual(res.status_code, 401),
                ]
            },
            {
                'auth': True,
                'data': {
                    "username": '1'
                },
                'assertions': [
                    # Change username to 1
                    lambda res: self.assertEqual(res.data['username'], '1'),
                ]
            },
            {
                'auth': True,
                'data': {
                    "shipping_address": {
                        "full_name": "vvvvaaaa",
                        "phone_number": "1234567890",
                        "email": "s@a.com",
                        "address": "222 St",
                        "province": "SK",
                        "postal_code": "M2W2W4"
                    }
                },
                'assertions': [
                    # Change related object
                    lambda res: self.assertEqual(
                        res.data['shipping_address']['province'], 'SK'),
                ]
            },
            {
                'auth': True,
                'data': {
                    "credit_card": '0120012001200120',
                    "shipping_address": {
                        "full_name": "vvvvaaaa",
                        "phone_number": "1234567890",
                        "email": "s@a.com",
                        "address": "222 St",
                        "province": "AB",
                        "postal_code": "M2W2W4"
                    }
                },
                'assertions': [
                    # Change both self and related object
                    lambda res: self.assertEqual(
                        res.data['shipping_address']['province'], 'AB'),
                    lambda res: self.assertEqual(
                        res.data['credit_card'], '0120012001200120'),
                ]
            },
            {
                'auth': True,
                'data': {
                    "credit_card": ''
                },
                'assertions': [
                    # Should not clear credit card once set
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

            res = self.client.patch('/api/users/', test['data'])
            for assertion in test['assertions']:
                assertion(res)


class ShippingAddressTest(APITestCase, AbstractTestSetup):
    @classmethod
    def setUpTestData(self):
        AbstractTestSetup.setup_user(self, signin=True)
        AbstractTestSetup.setup_ship_add(self)

    def test_get_address(self):
        tests_case = [
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
                    lambda res: [self.assertIn(field, res.data)
                                 for field in ('full_name', 'phone_number', 'email', 'address', 'province')],
                ]
            },
        ]

        for test in tests_case:
            if test['auth']:
                self.client.credentials(
                    HTTP_AUTHORIZATION='Token ' + self.token)
            else:
                self.client.credentials()

            res = self.client.get('/api/users/address/')
            for assertion in test['assertions']:
                assertion(res)

    def test_update_add(self):
        tests = [
            # Tests that do not require auth first
            {
                'auth': False,
                'full_name': "vvvvaaaa",
                'phone_number': "1234567890",
                'email': "aaa@a.com",
                'address': "222 St",
                'province': "ON",
                'postal_code': 'M2W2W2',
                'assertions': [
                    # Should not valid to unauthed user
                    lambda res: self.assertEqual(res.status_code, 401),
                ]
            },
            {
                'auth': True,
                'full_name': "vvvvaaaa",
                'phone_number': "123456789000000000000000000000000",
                'email': "aaa@a.com",
                'address': "222 St",
                'province': "ON",
                'postal_code': 'M2W2W2',
                'assertions': [
                    # invalid phone
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
            {
                'auth': True,
                'full_name': "vvvvaaaa",
                'phone_number': "1234567890",
                'email': "aaa",
                'address': "222 St",
                'province': "ON",
                'postal_code': 'M2W2W2',
                'assertions': [
                    # invalid email
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
            {
                'auth': True,
                'full_name': "++++++?",
                'phone_number': "1234567890",
                'email': "aaa@a.com",
                'address': "222 St",
                'province': "ON",
                'postal_code': 'M2W2W2',
                'assertions': [
                    # invalid name
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
            {
                'auth': True,
                'full_name': "++++++?",
                'phone_number': "1234567890",
                'email': "aaa@a.com",
                'address': "222 St",
                'province': "ON",
                'postal_code': 'M2W 2W2',
                'assertions': [
                    # invalid postal code
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
            {
                'auth': True,
                'full_name': "vvvvaaaa",
                'phone_number': "1234567890",
                'email': "aaa@a.com",
                'address': "222 St",
                'province': "ON",
                'postal_code': 'M2W2W2',
                'assertions': [
                    # successful
                    lambda res: self.assertGreaterEqual(res.status_code, 200),
                ]
            },
            {
                'auth': True,
                'full_name': "vvvvaaaa",
                'phone_number': "1234567890",
                'email': "aaa@a.com",
                'addr': "222 St",
                'province': "ON",
                'postal_code': 'M2W2W2',
                'assertions': [
                    # wrong field
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

            res = self.client.put('/api/users/address/')
            for assertion in test['assertions']:
                assertion(res)
