from django.urls import path

from .views import CartItemView

urlpatterns = [
    path(r'', CartItemView.as_view({
        'get': 'list',
        'post': 'create',
        'delete': 'destroy'
    })),
    path(r'<int:pk>/', CartItemView.as_view({
        'patch': 'partial_update',
    })),
]
