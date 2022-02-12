from django.urls import path
from .views import RecipesViewSet

urlpatterns=[
    path('', RecipesViewSet.as_view({
        'get': 'get_recipe',
    })),
]