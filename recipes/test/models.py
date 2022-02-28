from django.test import TestCase
from recipes.models import *
from project.setup_test import AbstractTestSetup

class TestRecipeModels(TestCase):

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

    #Test Recipe Models
    def test_recipe_names(self):
        self.assertEqual(str(self.recipes[0].name), "recipe1")
        self.assertEqual(str(self.recipes[1].name), "recipe2")
        self.assertEqual(str(self.recipes[2].name), "recipe3")

    def test_recipe_rating(self):
        self.assertEqual(str(self.recipes[0].rating), "5")
        self.assertEqual(str(self.recipes[1].rating), "4")
        self.assertEqual(str(self.recipes[2].rating), "3")

    def test_recipe_cuisine(self):
        self.assertEqual(str(self.recipes[0].cuisine), "greek")
        self.assertEqual(str(self.recipes[1].cuisine), "middleeast")
        self.assertEqual(str(self.recipes[2].cuisine), "thai")

    def test_recipe_total_review(self):
        self.assertEqual(str(self.recipes[0].total_reviews), "10")
        self.assertEqual(str(self.recipes[1].total_reviews), "5")
        self.assertEqual(str(self.recipes[2].total_reviews), "15")

    def test_recipe_products(self):
        self.assertEqual(str(self.recipes[0].products.get(pk=self.products[0].id).name), "test1")
        self.assertEqual(str(self.recipes[0].products.get(pk=self.products[1].id).name), "test2")
        self.assertEqual(str(self.recipes[1].products.get(pk=self.products[1].id).name), "test2")
        self.assertEqual(str(self.recipes[1].products.get(pk=self.products[2].id).name), "test3")
        self.assertEqual(str(self.recipes[2].products.get(pk=self.products[0].id).name), "test1")
        self.assertEqual(str(self.recipes[2].products.get(pk=self.products[1].id).name), "test2")
        self.assertEqual(str(self.recipes[2].products.get(pk=self.products[2].id).name), "test3")