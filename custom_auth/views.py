from django.contrib.auth import login

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response

from knox.views import LoginView as KnoxLoginView

from .serializers import ChangePasswordSerializer


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class ChangePasswordView(ModelViewSet):
    def create(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(
            data=request.data, context={'user': user})

        serializer.is_valid(raise_exception=True)

        user.set_password(request.data['new_password'])
        user.save()

        return Response()
