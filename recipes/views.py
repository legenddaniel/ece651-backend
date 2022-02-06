from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector, TrigramSimilarity

from .models import Recipe
from .serializers import RecipeSerializer

# Create your views here.
class RecipesViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    def recipe_list(self, request):
        print(request.query_params)
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

