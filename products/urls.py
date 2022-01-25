from django.urls import path
from .views import ProductsViewSet

urlpatterns=[
    path('all', ProductsViewSet.as_view({
        'get': 'list',
    })),
    path('<str:pk>', ProductsViewSet.as_view({
        'get': 'retrieve',
        # 'put': 'update',
        # 'delete': 'destroy',
    })),
]