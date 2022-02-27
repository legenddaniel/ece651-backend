from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector, TrigramSimilarity
from rest_framework.exceptions import ParseError

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer

# Create your views here.
class ProductsViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    def get_product(self, request):
        id = request.query_params.get('id', None)
        name = request.query_params.get('name', None)
        category = request.query_params.get('category', None)
        if id:
            product = Product.objects.all().filter(id=id)
            serializer = ProductDetailSerializer(product, many=True)
        elif name:
            searched_products = Product.objects.annotate(
                similarity=TrigramSimilarity('name', name) + TrigramSimilarity('description',name)).filter(
                similarity__gte=0.2).filter(is_active=True).order_by('-similarity')
            serializer = ProductSerializer(searched_products, many=True)
        elif category:
            searched_products = Product.objects.annotate(search=SearchVector('category__name'), ).filter(
                search=category).filter(is_active=True)
            serializer = ProductSerializer(searched_products, many=True)
        elif (len(request.query_params)==0 and (not id) and (not name) and (not category)):
            recipes = Product.objects.all().order_by('id')
            serializer = ProductSerializer(recipes, many=True)
        else:
            raise ParseError()
        return Response(serializer.data)