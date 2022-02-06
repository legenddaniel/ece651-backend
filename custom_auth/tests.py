from rest_framework.test import APITestCase
from knox.models import AuthToken

from users.models import User


class CustomAuthTest(APITestCase):
    email = 's@a.com'
    email2 = 'a@a.com'
    pwd = '12345678'

    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create_user(self.email, self.pwd)

    def test_signup(self):
        # Successful signup. We only use `email2` once here.
        response = self.client.post(
            '/api/auth/signup/',
            {
                'email': self.email2,
                'username': '123',
                'password': self.pwd
            }
        )
        self.assertEqual(response.status_code, 200,
                         'Status code is expected to be 200 for successful signup, got %s.' % response.status_code)
        self.assertIn('id', response.data)

        # Sign up with existing email
        response = self.client.post(
            '/api/auth/signup/',
            {
                'email': self.email,
                'username': '123',
                'password': self.pwd
            }
        )
        self.assertEqual(response.status_code, 400,
                         'Status code is expected be 400 for user-existed signup, got %s.' % response.status_code)

    def test_signin_signout(self):
        # Successful signin
        response = self.client.post(
            '/api/auth/signin/',
            {
                'username': self.email,
                'password': self.pwd
            }
        )
        self.assertTrue(
            {'expiry', 'token'} <= set(response.data),
            'Response data should contain "expiry" and "token", got %s.' % response.data
        )
        self.assertNotIn('password', response.data)
        for field in ('token', 'expiry', 'id', 'shipping_addresses', 'orders', 'cart_items', 'fav_recipes'):
            self.assertIn(field, response.data)

        # Wrong credentials
        response = self.client.post(
            '/api/auth/signin/',
            {
                'username': self.email,
                'password': 'asdasdas'
            }
        )
        self.assertGreaterEqual(response.status_code,
                                400, 'Status code should be 4xx for invalid credentials, got %s.' % response.status_code)

        # Invalid fields
        response = self.client.post(
            '/api/auth/signin/',
            {
                'email': self.email,
                'password': 'asdasdas'
            }
        )
        self.assertGreaterEqual(response.status_code,
                                400, 'Status code should be 4xx for invalid fields, got %s.' % response.status_code)

        # We only test valid user signout since it's fine to sign out a user not existing. Right now can't separate signin and signout tests.
        # token = AuthToken.objects.get(user=self.user)
        # response = self.client.post(
        #     '/api/auth/signout/',
        #     HTTP_AUTHORIZATION='Token ' + token.digest
        # )
        # self.assertEqual(response.status_code, 204,
        #                  'Status code is expected to be 204 for successful signout, got %s.' % response.status_code)

    def test_change_password(self):
        self.client.force_authenticate(user=self.user)

        # Successful change.
        response = self.client.post(
            '/api/auth/change_password/',
            {
                'old_password': self.pwd,
                'new_password': self.pwd
            }
        )
        self.assertEqual(response.status_code, 200,
                         'Status code is expected to be 200 for successful change password, got %s.' % response.status_code)

        # Wrong old password.
        response = self.client.post(
            '/api/auth/change_password/',
            {
                'old_password': 'dsdasds',
                'new_password': self.pwd
            }
        )
        self.assertEqual(response.status_code, 400,
                         'Status code is expected to be 400 for wrong password, got %s.' % response.status_code)

        # Invalid new password.
        response = self.client.post(
            '/api/auth/change_password/',
            {
                'old_password': self.pwd,
                'new_password': 'a-'
            }
        )
        self.assertEqual(response.status_code, 400,
                         'Status code is expected to be 400 for invalid password, got %s.' % response.status_code)
