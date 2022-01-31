from django.urls import path

from knox.views import LogoutView

from .views import LoginView, ChangePasswordView, RegistrationView

urlpatterns = [
    path(r'signin/', LoginView.as_view(), name='knox_login'),
    path(r'signout/', LogoutView.as_view(), name='knox_logout'),
    path(r'signup/',
         RegistrationView.as_view({'post': 'create'}), name='knox_logout'),
    path(r'change_password/',
         ChangePasswordView.as_view({'post': 'create'}), name='change_password'),
]
