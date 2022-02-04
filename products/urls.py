from django.urls import path
from .views import ProductsViewSet

urlpatterns=[
    path('all', ProductsViewSet.as_view({
        'get': 'product_list',
    })),
    path('<str:pk>', ProductsViewSet.as_view({
        'get': 'retrieve_product',
        # 'put': 'update',
        # 'delete': 'destroy',
    })),
    path('search/<str:search_keywords>', ProductsViewSet.as_view({
        'get': 'search_product',
        # 'put': 'update',
        # 'delete': 'destroy',
    })),
]