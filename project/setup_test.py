from abc import ABC


class AbstractTestSetup(ABC):
    ''' 
    Expose class members to the derived class.
    For example, you can access self.user in the derived class if you call AbstractTestSetup.setup_user(self) there.
    '''

    @staticmethod
    def setup_webdriver(self):
        from selenium import webdriver
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

        self.browser = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME)
        self.fe = 'http://lehstore'

    @staticmethod
    def setup_superuser(self, email='admin@test.com', password='12345678'):
        from users.models import User

        self.superuser = User.objects.create_superuser(email, password)

    @staticmethod
    def setup_user(self, email='test@test.com', password='12345678', signin=False):
        from users.models import User

        self.user = User.objects.create_user(email, password)

        if signin:
            from knox.models import AuthToken

            instance, token = AuthToken.objects.create(self.user)
            self.token = token

    @staticmethod
    def setup_products(self):
        from products.models import Product

        self.products = Product.objects.bulk_create([
            Product(
                name='test1',
                is_active=True,
                unit_quantity=100,
                price=100,
                stock=100,
                image_url='https://test.com/1.png',
                slug='test1'
            ),
            Product(
                name='test2',
                is_active=True,
                unit_quantity=33,
                price=33,
                stock=33,
                image_url='https://test.com/2.png',
                slug='test2'
            ),
            Product(
                name='test3',
                is_active=True,
                unit_quantity=55,
                price=55,
                stock=55,
                image_url='https://test.com/3.png',
                slug='test3'
            ),
        ])

    @staticmethod
    def setup_cart_items(self):

        from carts.models import CartItem

        self.cart_items = CartItem.objects.bulk_create([
            CartItem(
                user=self.user,
                product=self.products[0],
                quantity=5
            ),
            CartItem(
                user=self.user,
                product=self.products[1],
                quantity=6
            ),
        ])

    @staticmethod
    def setup_recipe(self):
        from recipes.models import Recipe, Nutrient

        self.recipes = Recipe.objects.bulk_create([
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
        self.recipes[0].products.set([self.products[0], self.products[1]])
        self.recipes[1].products.set([self.products[1], self.products[2]])
        self.recipes[2].products.set([self.products[0], self.products[1], self.products[2]])

        self.p1_nutrients = Nutrient.objects.create(recipe=self.recipes[0],
                                                   calories="100 cal")
        self.p2_nutrients = Nutrient.objects.create(recipe=self.recipes[1],
                                                   calories="200 cal")
        self.p3_nutrients = Nutrient.objects.create(recipe=self.recipes[2],
                                                   calories="300 cal")
    
    @staticmethod
    def setup_ship_add(self):

        from users.models import ShippingAddress

        self.shipping_address = ShippingAddress.objects.create(
            user=self.user,
            full_name="aaa",
            phone_number="1234567890",
            email="a@a.com",
            address="First St",
            province="ON"
        )

    @staticmethod
    def setup_orders(self):

        from orders.models import Order, OrderItem
        from decimal import Decimal

        subtotal = self.products[0].price + self.products[1].price
        order = {
            'user': self.user,
            'status': 'unpaid',
            'subtotal': subtotal,
            'tax': subtotal * Decimal(0.13),
            'total': subtotal * Decimal(1.13),
        }
        self.orders = Order.objects.bulk_create([
            Order(**order),
            Order(**order),
        ])

        OrderItem.objects.bulk_create([
            OrderItem(
                order=self.orders[0],
                product=self.products[0],
                quantity=1,
                unit_price=self.products[0].price,
            ),
            OrderItem(
                order=self.orders[0],
                product=self.products[1],
                quantity=1,
                unit_price=self.products[1].price,
            ),
            OrderItem(
                order=self.orders[1],
                product=self.products[0],
                quantity=1,
                unit_price=self.products[0].price,
            ),
            OrderItem(
                order=self.orders[1],
                product=self.products[1],
                quantity=1,
                unit_price=self.products[1].price,
            ),
        ])
