from django.test import TestCase
from products.models import Product, ProductTag, ProductCategory, ProductNutrient

class TestProductModels(TestCase):

    @classmethod
    def setUpTestData(cls):

        pcat1 = ProductCategory.objects.create(name="Vegetables")
        ptag1 = ProductTag.objects.create(name="Low in Sodium")
        cls.product1 = Product.objects.create(name="Lettuce", category=pcat1,
                                              description="Healthy Lettuce", si_unit="gram",
                                              unit_quantity="300", is_active=True,
                                              price=4.99, stock=100, on_promotion=False,
                                              in_recipe=True,
                                              image_url='www.google.com', slug="lettuce")
        cls.product1.labels.set([ptag1])

    def test_product_category_str(self):
        self.assertEqual(str(self.product1.name), "Lettuce")
