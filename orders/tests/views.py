from rest_framework.test import APITestCase

from project.setup_test import AbstractTestSetup


class OrderTest(APITestCase, AbstractTestSetup):
    @classmethod
    def setUpTestData(self):
        AbstractTestSetup.setup_user(self, signin=True)
        AbstractTestSetup.setup_products(self)
        AbstractTestSetup.setup_orders(self)

    def test_list_orders(self):
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
                                 for field in ('id', 'order_items', 'created', 'status', 'subtotal')],

                    # Should belong to current user
                    lambda res: self.assertEqual(
                        res.data[0]['user'], self.user.id),

                    # Should contain order item details
                    lambda res: [self.assertIn(field, res.data[0]['order_items'][0])
                                 for field in ('id', 'quantity', 'unit_price', 'product')],

                    # Should contain product details
                    lambda res: [self.assertIn(field, res.data[0]['order_items'][0]['product'])
                                 for field in ('id', 'name', 'price', 'stock', 'image_url', 'description')],
                ]
            },
        ]

        for test in tests:
            if test['auth']:
                self.client.credentials(
                    HTTP_AUTHORIZATION='Token ' + self.token)
            else:
                self.client.credentials()

            res = self.client.get('/api/orders/')
            for assertion in test['assertions']:
                assertion(res)

    def test_get_order(self):
        tests = [
            # Tests that do not require auth first
            {
                'auth': False,
                'order_id': self.orders[0].id,
                'assertions': [
                    # Should not valid to unauthed user
                    lambda res: self.assertEqual(
                        res.status_code, 401),
                ]
            },
            {
                'auth': True,
                'order_id': 1312323,
                'assertions': [
                    # Wrong order id
                    lambda res: self.assertGreaterEqual(
                        res.status_code, 400),
                ]
            },
            {
                'auth': True,
                'order_id': self.orders[0].id,
                'assertions': [
                    # Should contain some fields
                    lambda res: [self.assertIn(field, res.data)
                                 for field in ('id', 'order_items', 'created', 'status', 'subtotal')],

                    # Should belong to current user
                    lambda res: self.assertEqual(
                        res.data['user'], self.user.id),

                    # Should contain order item details
                    lambda res: [self.assertIn(field, res.data['order_items'][0])
                                 for field in ('id', 'quantity', 'unit_price', 'product')],

                    # Should contain product details
                    lambda res: [self.assertIn(field, res.data['order_items'][0]['product'])
                                 for field in ('id', 'name', 'price', 'stock', 'image_url', 'description')],
                ]
            },
        ]

        for test in tests:
            if test['auth']:
                self.client.credentials(
                    HTTP_AUTHORIZATION='Token ' + self.token)
            else:
                self.client.credentials()

            res = self.client.get('/api/orders/%d/' % test['order_id'])
            for assertion in test['assertions']:
                assertion(res)

    def test_create_order(self):
        tests = [
            # Tests that do not require auth first
            {
                'auth': False,
                'data': {
                    "status": "unpaid",
                    "order_items": [
                        {
                            "product_id": self.products[0].id,
                            "quantity": 1
                        },
                        {
                            "product_id": self.products[1].id,
                            "quantity": 2
                        }
                    ]
                },
                'assertions': [
                    # Should not valid to unauthed user
                    lambda res: self.assertEqual(res.status_code, 401),
                ]
            },
            {
                'auth': True,
                'data': {
                    "status": "unpaid",
                    "order_items": [
                        {
                            "product_id": 1342,
                            "quantity": 1
                        },
                        {
                            "product_id": self.products[1].id,
                            "quantity": 2
                        }
                    ]
                },
                'assertions': [
                    # Should not add a invalid product to order
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
            {
                'auth': True,
                'data': {
                    "status": "unpaid",
                    "order_items": [
                        {
                            "product_id": self.products[0].id,
                            "quantity": 15345435453
                        },
                        {
                            "product_id": self.products[1].id,
                            "quantity": 2
                        }
                    ]
                },
                'assertions': [
                    # Should not add product more than stock
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
            {
                'auth': True,
                'data': {
                    "status": "asd",
                    "order_items": [
                        {
                            "product_id": self.products[0].id,
                            "quantity": 1
                        },
                        {
                            "product_id": self.products[1].id,
                            "quantity": 2
                        }
                    ]
                },
                'assertions': [
                    # Wrong status
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
            {
                'auth': True,
                'data': {
                    "status": "unpaid",
                    "order_items": [
                        {
                            "product_id": self.products[0].id,
                            "quantity": 1
                        },
                        {
                            "product_id": self.products[1].id,
                            "quantity": 2
                        }
                    ]
                },
                'assertions': [
                    # Add a new order
                    lambda res: self.assertEqual(len(res.data), 3),
                ]
            },
        ]

        for test in tests:
            if test['auth']:
                self.client.credentials(
                    HTTP_AUTHORIZATION='Token ' + self.token)
            else:
                self.client.credentials()

            res = self.client.post('/api/orders/', test['data'])
            for assertion in test['assertions']:
                assertion(res)

    def test_update_order(self):
        tests = [
            # Tests that do not require auth first
            {
                'auth': False,
                'order_id': self.orders[0].id,
                'data': {
                    "status": 'completed'
                },
                'assertions': [
                    # Should not valid to unauthed user
                    lambda res: self.assertEqual(res.status_code, 401),
                ]
            },
            {
                'auth': True,
                'order_id': self.orders[0].id,
                'data': {
                    "status": 'completed'
                },
                'assertions': [
                    # Change first order to completed
                    lambda res: self.assertEqual(
                        res.data[0]['status'], 'completed'),
                ]
            },
            {
                'auth': True,
                'order_id': self.orders[0].id,
                'data': {
                    "status": 'complet'
                },
                'assertions': [
                    # Wrong status
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
            {
                'auth': True,
                'order_id': 1312312,
                'data': {
                    "status": 'completed'
                },
                'assertions': [
                    # Invalid order id
                    lambda res: self.assertEqual(res.status_code, 404),
                ]
            },
            {
                'auth': True,
                'order_id': self.orders[0].id,
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

            res = self.client.patch('/api/orders/%d/' %
                                    test['order_id'], test['data'])
            for assertion in test['assertions']:
                assertion(res)
