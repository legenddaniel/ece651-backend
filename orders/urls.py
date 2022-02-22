from django.urls import path

from .views import OrderView

urlpatterns = [
    path(r'', OrderView.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path(r'<int:order_id>/', OrderView.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
    })),
]
