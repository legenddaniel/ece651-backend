from ast import Add
from django.shortcuts import redirect, render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector, TrigramSimilarity
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from .models import ShippingAddress,User
from recipes.models import Recipe
from .serializers import AddressSerializers,FavouriteSerializers


class AddressView(viewsets.ViewSet):
    #permission_classes = (AllowAny,)
    
    
    def get(self,request):
        # if not request.user.is_authenticated:
        #     return redirect("login")
        
        origin_address = ShippingAddress.objects.filter(user = self.request.user)
        
        serializer = AddressSerializers(origin_address,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        
        
        ship_add = ShippingAddress.objects.filter(user = self.request.user).first()
        
        serializer = AddressSerializers(ship_add, data = request.data) 
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
    
    def put(self,request, *args, **kwargs):
        
        ship_update = ShippingAddress.objects.filter(user = self.request.user).first()
        serializer = AddressSerializers(ship_update, data = request.data)  #instance = new_add
        message= {}
        
        if serializer.is_valid():
            serializer.save()
            message["success"] = "updated"
            return Response(data = message)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        pass
        
    

class FavouriteView(viewsets.ViewSet):
    
    serializer_class = FavouriteSerializers
    def get_fav(self,request):
        favourite_list = User.objects.all()    #Recipe.objects.all()
        return favourite_list
    
    def create(self,request, *args, **kwargs):
        
        serializer = AddressSerializers(data = request.data) 
        
        data = request.data
        
        for recipe_temp in data["fav_recipes"]:
            recipe_obj  = Recipe.objects.get(name = recipe_temp["name"])
            User.fav_recipes.add(recipe_obj)
        
        
        
        return Response(serializer)