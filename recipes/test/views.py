from django.test import TestCase
from recipes.models import *
from project.setup_test import AbstractTestSetup

class TestRecipeViews(TestCase):

    #Set up test
    @classmethod
    def setUpTestData(cls):
        AbstractTestSetup.setup_products(cls)

        cls.recipes = Recipe.objects.bulk_create([
            Recipe(
                name='recipe1',
                rating=5,
                cuisine='greek',
                image_url='https://test.com/1.png',
                total_reviews=10,
                slug='recipe1'
            ),
            Recipe(
                name='recipe2',
                rating=4,
                cuisine='middleeast',
                image_url='https://test.com/2.png',
                total_reviews=5,
                slug='recipe2'
            ),
            Recipe(
                name='recipe3',
                rating=3,
                cuisine='thai',
                image_url='https://test.com/3.png',
                total_reviews=15,
                slug='recipe3'
            ),
        ])
        cls.recipes[0].products.set([cls.products[0], cls.products[1]])
        cls.recipes[1].products.set([cls.products[1], cls.products[2]])
        cls.recipes[2].products.set([cls.products[0], cls.products[1], cls.products[2]])

        cls.p1_nutrients = Nutrient.objects.create(recipe=cls.recipes[0],
                                                   calories="100 cal")
        cls.p2_nutrients = Nutrient.objects.create(recipe=cls.recipes[1],
                                                   calories="200 cal")
        cls.p3_nutrients = Nutrient.objects.create(recipe=cls.recipes[2],
                                                   calories="300 cal")

    #Test Recipe API
    def test_get_recipes_lists(self):
        res1 = self.client.get('/api/recipes/')
        self.assertEqual(res1.status_code, 200)
        res2 = self.client.get('/api/recipe/')
        self.assertGreaterEqual(res2.status_code, 400)

    def test_get_recipes_by_name(self):
        res1 = self.client.get('/api/recipes/?name=recipe1/')
        self.assertEqual(res1.status_code, 200)
        self.assertEqual(res1.data[0]['name'], 'recipe1')
        res2 = self.client.get('/api/recipes/?name=recipe/')
        self.assertEqual(res2.status_code, 200)
        self.assertEqual(res2.data[0]['name'], 'recipe1')
        res3 = self.client.get('/api/recipes/?name=randomname/')
        self.assertEqual(res3.status_code, 200)
        self.assertEqual(len(res3.data), 0)
        res4 = self.client.get('/api/recipes/?name=test/')
        self.assertEqual(res4.status_code, 200)
        self.assertGreaterEqual(len(res4.data), 0)

    def test_get_recipes_by_id(self):
        res1 = self.client.get('/api/recipes/?id='+str(self.recipes[0].id))
        self.assertEqual(res1.status_code, 200)
        self.assertEqual(res1.data[0]['name'], 'recipe1')
        res2 = self.client.get('/api/recipes/?id='+str(self.recipes[1].id))
        self.assertEqual(res2.status_code, 200)
        self.assertEqual(res2.data[0]['name'], 'recipe2')
        res3 = self.client.get('/api/recipes/?id='+str(self.recipes[2].id + 1))
        self.assertEqual(res3.status_code, 200)
        self.assertEqual(len(res3.data), 0)