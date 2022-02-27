from rest_framework.test import APITestCase
from knox.models import AuthToken

from project.setup_test import AbstractTestSetup
# Create your tests here.

class CustomAuthTest(APITestCase, AbstractTestSetup):
    @classmethod
    def setUpTestData(self):
        AbstractTestSetup.setup_user(self, signin=False)
        AbstractTestSetup.setup_ship_add(self)
        
        def test_get_address(self):
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
                                 for field in ('full_name', 'phone_number', 'email','address','province')],

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

            res = self.client.get('/users/address/')
            for assertion in test['assertions']:
                assertion(res)

    
    
    # def test_update_add(self):
    #     tests = [
    #         # Tests that do not require auth first
    #         {
    #             'auth': False,
    #             'full_name': "vvvvaaaa",
    #             'phone_number':"1234567890",
    #             'email': "aaa@a.com",
    #             'address': "222 St",
    #             'province':"ON",
    #             'assertions': [
    #                 # Should not valid to unauthed user
    #                 lambda res: self.assertEqual(res.status_code, 401),
    #             ]
    #         },
    #         {
    #             'auth': True,
    #             'full_name': "vvvvaaaa",
    #             'phone_number':"123456789000000000000000000000000",
    #             'email': "aaa@a.com",
    #             'address': "222 St",
    #             'province':"ON",
    #             'assertions': [
    #                 # invalid phone
    #                 lambda res: self.assertEqual(res.status.code,400),
    #             ]
    #         },
    #         {
    #             'auth': True,
    #             'full_name': "vvvvaaaa",
    #             'phone_number':"1234567890",
    #             'email': "aaa",
    #             'address': "222 St",
    #             'province':"ON",
    #             'assertions': [
    #                 # invalid email
    #                 lambda res: self.assertEqual(res.status.code,400),
    #             ]
    #         },
    #         {
    #             'auth': True,
    #             'full_name': "++++++?",
    #             'phone_number':"1234567890",
    #             'email': "aaa@a.com",
    #             'address': "222 St",
    #             'province':"ON",
    #             'assertions': [
    #                 # invalid name
    #                 lambda res: self.assertEqual(res.status.code,400),
    #             ]
    #         },
    #         {
    #             'auth': True,
    #             'full_name': "vvvvaaaa",
    #             'phone_number':"1234567890",
    #             'email': "aaa@a.com",
    #             'address': "222 St",
    #             'province':"ON",
    #             'assertions': [
    #                 # successful
    #                 lambda res: self.assertGreaterEqual(res.status_code, 200),
    #             ]
    #         },
    #         {
    #             'auth': True,
    #             'full_name': "vvvvaaaa",
    #             'phone_number':"1234567890",
    #             'email': "aaa@a.com",
    #             'addr': "222 St",
    #             'province':"ON",
    #             'assertions': [
    #                 # wrong field
    #                 lambda res: self.assertGreaterEqual(res.status_code, 400),
    #             ]
    #         },
    #     ]

    #     for test in tests:
    #         if test['auth']:
    #             self.client.credentials(
    #                 HTTP_AUTHORIZATION='Token ' + self.token)
    #         else:
    #             self.client.credentials()

    #         res = self.client.put('/users/address/update/')
    #         for assertion in test['assertions']:
    #             assertion(res)
