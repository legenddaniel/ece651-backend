from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector, TrigramSimilarity
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer

# Create your views here.
class ProductsViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def product_list(self, request):
        products = Product.objects.all().filter(is_active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def retrieve_product(self, request, pk=None):
        product = Product.objects.get(product_id=pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

    #Install TrigramExtension to use TrigramSimilarity;
    #Add a custom migration file and include TrigramExtension()
    def search_product(self, request, search_keywords=None):
        # search_keywords = request.GET.get('keywords')
        searched_products = Product.objects.annotate(similarity=TrigramSimilarity('name',search_keywords)+TrigramSimilarity('description',search_keywords)).filter(similarity__gte=0.2).filter(is_active=True).order_by('-similarity')
        serializer = ProductSerializer(searched_products, many=True)
        return Response(serializer.data)

    def category_product(self, request, category_name=None):
        searched_products = Product.objects.annotate(search = SearchVector('category__name'),).filter(search=category_name).filter(is_active=True)
        serializer = ProductSerializer(searched_products, many=True)
        return Response(serializer.data)
