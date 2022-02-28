from django.test import TestCase
from rest_framework.test import APITestCase
from project.setup_test import AbstractTestSetup


class TestProductView(AbstractTestSetup, APITestCase):
    @classmethod
    def setUpTestData(self):
        AbstractTestSetup.setup_products(self)

    def test_get_product_lists(self):
        res1 = self.client.get('/api/products/')
        self.assertEqual(res1.status_code, 200)
        res2 = self.client.get('/api/product/')
        self.assertGreaterEqual(res2.status_code, 400)

    def test_get_product_by_name(self):
        res1 = self.client.get('/api/products/?name=test1/')
        self.assertEqual(res1.status_code, 200)
        self.assertEqual(res1.data[0]['name'], 'test1')
        res2 = self.client.get('/api/products/?name=test/')
        self.assertEqual(res2.status_code, 200)
        self.assertEqual(res2.data[0]['name'], 'test1')
        res3 = self.client.get('/api/products/?name=randomname/')
        self.assertEqual(res3.status_code, 200)
        self.assertEqual(len(res3.data), 0)
        res4 = self.client.get('/api/products/?name=test/')
        self.assertEqual(res4.status_code, 200)
        self.assertGreaterEqual(len(res4.data), 0)

    def test_get_product_by_id(self):
        res1 = self.client.get('/api/products/?id='+str(self.products[0].id))
        self.assertEqual(res1.status_code, 200)
        self.assertEqual(res1.data[0]['name'], 'test1')
        res2 = self.client.get('/api/products/?id='+str(self.products[1].id))
        self.assertEqual(res2.status_code, 200)
        self.assertEqual(res2.data[0]['name'], 'test2')
        res3 = self.client.get('/api/products/?id='+str(self.products[2].id + 1))
        self.assertEqual(res3.status_code, 200)
        self.assertEqual(len(res3.data), 0)
