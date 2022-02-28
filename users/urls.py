from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    
    path(r'address/',views.AddressView.as_view({'get':'get'}),name='get_address'),
    path(r'address/add/',views.AddressView.as_view({'post':'post'}),name='add_address'),
    path(r'address/update/',views.AddressView.as_view({'put':'put'}),name='update_address'),
    
    
]

    