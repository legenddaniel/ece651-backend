from django.test import TestCase
from products.models import Product, ProductTag, ProductCategory

class TestProductModels(TestCase):

    #Set up test
    @classmethod
    def setUpTestData(cls):
        pcat1 = ProductCategory.objects.create(name="Vegetables")
        plabel1 = ProductTag.objects.create(name="Low in Sodium")
        plabel2 = ProductTag.objects.create(name="High in Protein")
        cls.product1 = Product.objects.create(name="Lettuce", category=pcat1,
                                              description="Healthy Lettuce", si_unit="gram",
                                              unit_quantity=300, is_active=True,
                                              price=4.99, stock=100, on_promotion=False,
                                              in_recipe=True,
                                              image_url='www.google.com', slug="lettuce")
        cls.product1.category = pcat1
        cls.product1.labels.set([plabel1.pk, plabel2.pk])
        cls.pcat1 = pcat1
        cls.plabel1 = plabel1

    #Test Product
    def test_product_str(self):
        self.assertEqual(str(self.product1), "Lettuce")

    def test_product_description(self):
        self.assertEqual(str(self.product1.description), "Healthy Lettuce")

    def test_product_unit(self):
        self.assertEqual(str(self.product1.si_unit), "gram")

    def test_product_unit_quantity(self):
        self.assertEqual(str(self.product1.unit_quantity), "300")

    def test_product_is_active(self):
        self.assertEqual(str(self.product1.is_active), 'True')

    def test_product_price(self):
        self.assertEqual(str(self.product1.price), "4.99")

    def test_product_stock(self):
        self.assertEqual(str(self.product1.stock), "100")

    def test_product_on_promotion(self):
        self.assertEqual(str(self.product1.on_promotion), "False")

    def test_product_in_recipe(self):
        self.assertEqual(str(self.product1.in_recipe), "True")

    def test_product_image_url(self):
        self.assertEqual(str(self.product1.image_url), "www.google.com")

    def test_product_slug(self):
        self.assertEqual(str(self.product1.slug), "lettuce")

    #Test Product Category
    def test_category_str(self):
        self.assertEqual(str(self.pcat1), "Vegetables")

    def test_product_category_str(self):
        self.assertEqual(str(self.product1.category), "Vegetables")

    #Test Product Labels (Tags)
    def test_label_str(self):
        self.assertEqual(str(self.plabel1), "Low in Sodium")

    def test_product_label(self):
        self.assertEqual(self.product1.labels.count(), 2)

    def test_product_label_name1(self):
        self.assertEqual(self.product1.labels.get(pk=1).name, "Low in Sodium")

    def test_product_label_name2(self):
        # print(self.product1.labels.get(name="High in Protein"))
        self.assertEqual(self.product1.labels.get(name="High in Protein").name, "High in Protein")