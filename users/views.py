from django.shortcuts import redirect, render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector, TrigramSimilarity
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from .models import ShippingAddress
from .serializers import AddressSerializers


class AddressView(viewsets.ViewSet):
    #permission_classes = (AllowAny,)
    
    def get(self,request):
        # if not request.user.is_authenticated:
        #     return redirect("login")
        
        origin_address = ShippingAddress.objects.all()
        
        serializer = AddressSerializers(origin_address,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        
        receiver = request.user
        ship_add = ShippingAddress(user= receiver)
        
        serializer = AddressSerializers(ship_add, data = request.data) 
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
    
    def put(self,request):
        
        serializer = AddressSerializers(data = request.data)  #instance = new_add
        data = {}
        
        if serializer.is_valid():
            serializer.save()
            data["success"] = "updated"
            return Response(data = data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        pass