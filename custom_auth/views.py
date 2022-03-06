from django.contrib.auth import login

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from knox.views import LoginView as KnoxLoginView

from .serializers import ChangePasswordSerializer, RegistrationSerializer, LoginSerializer


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request, serializer.validated_data['user'])

        login_res = super(LoginView, self).post(request, format=None)

        return Response({
            **login_res.data,
            **serializer.data['user'],
        })


class RegistrationView(ModelViewSet):
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({'id': user.pk})


class ChangePasswordView(ModelViewSet):
    def create(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(
            data=request.data, context={'user': user})

        serializer.is_valid(raise_exception=True)

        user.set_password(request.data['new_password'])
        user.save()

        return Response()
