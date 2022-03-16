from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.UserView.as_view({
        'get': 'retrieve',
        'patch': 'partial_update'
    }), name='user'),
    # path(r'address/', views.ShippingAddressView.as_view({
    #     'get': 'retrieve',
    #     'put': 'put'
    # }), name='get_address'),
]
