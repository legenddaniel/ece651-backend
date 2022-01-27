from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products
from .serializers import ProductsSerializer
import random

# Create your views here.
class ProductsViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = Products.objects.get(products_id=pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)