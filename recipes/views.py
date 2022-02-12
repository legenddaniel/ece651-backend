from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.postgres.search import TrigramSimilarity
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.exceptions import ParseError

# Create your views here.
class RecipesViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    def get_recipe(self, request):
        id = request.query_params.get('id', None)
        name = request.query_params.get('name', None)
        cuisine = request.query_params.get('cuisine', None)
        if id:
            recipes = Recipe.objects.all().filter(id=id)
            serializer = RecipeSerializer(recipes, many=True)
        elif name:
            recipes = Recipe.objects.annotate(similarity=TrigramSimilarity('name',name)+TrigramSimilarity('description',name)).filter(similarity__gte=0.2).order_by('-similarity')
            serializer = RecipeSerializer(recipes, many=True)
        elif cuisine:
            recipes = Recipe.objects.all().filter(cuisine__iexact=cuisine)
            serializer = RecipeSerializer(recipes, many=True)
        elif (len(request.query_params)==0 and (not id) and (not name) and (not cuisine)):
            recipes = Recipe.objects.all()
            serializer = RecipeSerializer(recipes, many=True)
        else:
            raise ParseError()
        return Response(serializer.data)

