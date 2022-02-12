from rest_framework import serializers
from .models import Recipe, Nutrient, ProductQuantity
from products.models import Product

class RecipeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','image_url', 'price']

class RecipeProductIDListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        r = super().to_representation(data)
        return { item['id'] for item in r }

class RecipeProductIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id']
        list_serializer_class = RecipeProductIDListSerializer

class RecipeQuantityListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        r = super().to_representation(data)
        return { item['product_name']: item['quantity'] for item in r }

class RecipeQuantitySerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    class Meta:
        model = ProductQuantity
        fields = ['product_name', 'quantity',]
        list_serializer_class = RecipeQuantityListSerializer

class RecipeNutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = ['calories', 'total_fat', 'saturated_fat', 'cholesterol', 'sodium', 'total_fiber', 'protein', 'carbohydrates', 'potassium']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients_product = serializers.SerializerMethodField()
    ingredients_id = serializers.SerializerMethodField('get_alternate_name')
    details = serializers.SerializerMethodField()
    quantity = RecipeQuantitySerializer(source='productquantity_set', many=True)

    def get_ingredients_product(self, obj):
        selected_products = Product.objects.filter(
            recipe_products__name=obj).all()
        return RecipeProductSerializer(selected_products, many=True).data

    def get_details(self, obj):
        return {'instruction': obj.instructions,
                'nutrients': RecipeNutrientSerializer(obj.nutrient).data,
                # 'quantity': RecipeQuantitySerializer(obj.productquantity_set, many=True).data,
                }

    def get_alternate_name(self, obj):
        return RecipeProductIDSerializer(obj.products, many=True).data

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'details', 'image_url', 'cuisine', 'ingredients_id', 'ingredients_product', 'rating', 'total_reviews', 'quantity']

    def to_representation(self, instance):
        data = super(RecipeSerializer, self).to_representation(instance)
        this_dict = {}
        for name, quant in data.pop('quantity').items():
            this_dict.update({name:quant})
        data.get('details').update({'quantity':this_dict})
        return data



