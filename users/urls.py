from django.urls import path

from knox.views import LogoutView

from .views import LoginView, ChangePasswordView

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='knox_login'),
    path(r'logout/', LogoutView.as_view(), name='knox_logout'),
    path(r'change_password/',
         ChangePasswordView.as_view({'post': 'create'}), name='change_password'),
]
