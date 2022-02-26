from ast import Add
from django.shortcuts import redirect, render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.viewsets import ModelViewSet
from .models import ShippingAddress

from .serializers import AddressSerializers


class AddressView(ModelViewSet):
    #permission_classes = (AllowAny,)
    serializer_class = AddressSerializers
    
    def get(self,request):
        
        origin_address = ShippingAddress.objects.filter(user = self.request.user)
        print(origin_address)
        serializer = AddressSerializers(origin_address,many = True)
        
        return Response(serializer.data)
        # curr_user = request.user
        # return ShippingAddress.objects.filter(user = curr_user)
    
    def post(self,request):
        
        ship_add = ShippingAddress.objects.filter(user = request.user).first()
        request.data['user'] = request.user.id
        serializer = AddressSerializers(ship_add, data = request.data) 
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
    
    def put(self,request):
        
        ship_update = ShippingAddress.objects.filter(user = request.user).first()
        request.data['user'] = request.user.id
        serializer = AddressSerializers(ship_update, data = request.data)  #instance = new_add
        message= {}
        
        if serializer.is_valid():
            serializer.save()
            message["success"] = "updated"
            return Response(data = message)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        pass
        
    

