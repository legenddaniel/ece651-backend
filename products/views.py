from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
import random

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
        searched_products = Product.objects.filter(Q(name__icontains=search_keywords) | Q(category__name__icontains=search_keywords))
        serializer = ProductSerializer(searched_products, many=True)
        return Response(serializer.data)
