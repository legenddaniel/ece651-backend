from rest_framework.test import APITestCase
from knox.models import AuthToken

from project.setup_test import AbstractTestSetup


class CustomAuthTest(APITestCase, AbstractTestSetup):
    @classmethod
    def setUpTestData(self):
        AbstractTestSetup.setup_user(self, signin=False)

    def test_signup(self):
        tests = [
            {
                'data': {
                    'email': 'test2@test.com',
                    'username': '123',
                    'password': '12345678'
                },
                'assertions': [
                    # Valid email
                    lambda res: self.assertIn('id', res.data),
                    lambda res: self.assertNotIn('password', res.data)
                ]
            },
            {
                'data': {
                    'email': self.user.email,
                    'username': '123',
                    'password': '12345678'
                },
                'assertions': [
                    # Existing user
                    lambda res: self.assertEqual(res.status_code, 400)
                ]
            },
            {
                'data': {
                    'email': 'sdas',
                    'username': '123',
                    'password': '12345678'
                },
                'assertions': [
                    # Invalid email
                    lambda res: self.assertEqual(res.status_code, 400)
                ]
            },
            {
                'data': {
                    'email': 'test2@test.com',
                    'username': '123',
                    'password': 'INSERT INTO users_user VALUES ()'
                },
                'assertions': [
                    # Invalid password
                    lambda res: self.assertEqual(res.status_code, 400)
                ]
            },
        ]

        for test in tests:
            res = self.client.post('/api/auth/signup/', test['data'])
            for assertion in test['assertions']:
                assertion(res)

    def test_signin(self):
        tests = [
            {
                'data': {
                    'username': self.user.email,
                    'password': '12345678'
                },
                'assertions': [
                    # Successful signin
                    lambda res: [self.assertIn(field, res.data) for field in (
                        'token', 'id', 'username', 'email')],
                    lambda res: self.assertNotIn('password', res.data)
                ]
            },
            {
                'data': {
                    'username': self.user.email,
                    'password': '1234567'
                },
                'assertions': [
                    # Wrong credentials
                    lambda res: self.assertEqual(res.status_code, 400)
                ]
            },
            {
                'data': {
                    'email': self.user.email,
                    'password': '12345678'
                },
                'assertions': [
                    # Wrong field
                    lambda res: self.assertGreaterEqual(res.status_code, 400)
                ]
            },
        ]

        for test in tests:
            res = self.client.post('/api/auth/signin/', test['data'])
            for assertion in test['assertions']:
                assertion(res)

    def test_signout(self):
        tests = [
            {
                'auth': False,
                'assertions': [
                    # Invalid token
                    lambda res: self.assertEqual(res.status_code, 401)
                ]
            },
            {
                'auth': True,
                'assertions': [
                    # Successful signout
                    lambda res: self.assertEqual(res.status_code, 204)
                ]
            },
        ]

        # Generate token

        instance, token = AuthToken.objects.create(self.user)
        for test in tests:
            if test['auth']:
                self.client.credentials(
                    HTTP_AUTHORIZATION='Token ' + token)
            else:
                self.client.credentials()

            res = self.client.post('/api/auth/signout/')
            for assertion in test['assertions']:
                assertion(res)

    def test_change_password(self):
        tests = [
            {
                'auth': False,
                'data': {
                    'old_password': '12345678',
                    'new_password': '12345678',
                },
                'assertions': [
                    # Should not valid to unauthed user
                    lambda res: self.assertEqual(res.status_code, 401),
                ]
            },
            {
                'auth': True,
                'data': {
                    'old_password': '12345678',
                    'new_password': '12345678',
                },
                'assertions': [
                    # Successful change password
                    lambda res: self.assertEqual(res.status_code, 200),
                ]
            },
            {
                'auth': True,
                'data': {
                    'old_password': '1234567',
                    'new_password': '12345678',
                },
                'assertions': [
                    # Wrong old password
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
            {
                'auth': True,
                'data': {
                    'old_passwor': '12345678',
                    'new_password': '12345678',
                },
                'assertions': [
                    # Wrong field
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
            {
                'auth': True,
                'data': {
                    'old_password': '12345678',
                    'new_password': '*-/--*',
                },
                'assertions': [
                    # Invalid password
                    lambda res: self.assertEqual(res.status_code, 400),
                ]
            },
        ]

        instance, token = AuthToken.objects.create(self.user)
        for test in tests:
            if test['auth']:
                self.client.credentials(
                    HTTP_AUTHORIZATION='Token ' + token)
            else:
                self.client.credentials()

            res = self.client.post('/api/auth/change_password/', test['data'])
            for assertion in test['assertions']:
                assertion(res)
