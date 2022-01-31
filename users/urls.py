from django.urls import path

from knox.views import LogoutView

from .views import LoginView

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='knox_login'),
    path(r'logout/', LogoutView.as_view(), name='knox_logout'),
]
