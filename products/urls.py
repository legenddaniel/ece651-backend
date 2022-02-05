from django.urls import path
from .views import ProductsViewSet

urlpatterns=[
    path('', ProductsViewSet.as_view({
        'get': 'product_list',
    })),
    path('<str:pk>/', ProductsViewSet.as_view({
        'get': 'retrieve_product',
    })),
    path('search/<str:search_keywords>', ProductsViewSet.as_view({
        'get': 'search_product',
    })),
    path('category/<str:category_name>/', ProductsViewSet.as_view({
        'get': 'category_product',
    })),
]