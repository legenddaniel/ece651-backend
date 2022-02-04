from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, TrigramSimilarity
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer

# Create your views here.
class ProductsViewSet(viewsets.ViewSet):
    def product_list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def retrieve_product(self, request, pk=None):
        product = Product.objects.get(product_id=pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

    def search_product(self, request, search_keywords=None):
        searched_products = Product.objects.annotate(similarity=TrigramSimilarity('name',search_keywords)+TrigramSimilarity('description',search_keywords)).filter(similarity__gte=0.2).order_by('-similarity')
        serializer = ProductSerializer(searched_products, many=True)
        return Response(serializer.data)

    def category_product(self, request, category_name=None):
        searched_products = Product.objects.annotate(search = SearchVector('category__name'),).filter(search=category_name)
        serializer = ProductSerializer(searched_products, many=True)
        return Response(serializer.data)
