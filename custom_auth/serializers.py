from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

from users.models import User
from project.validators import CustomValidator

from users.serializers import UserSerializer


class LoginSerializer(AuthTokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'email', 'username']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'username': {'required': True},
        }

    password = serializers.CharField(
        min_length=8, write_only=True, required=True, validators=[CustomValidator.alphanumeric])

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('old_password', 'new_password')

    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(
        min_length=8, write_only=True, required=True, validators=[CustomValidator.alphanumeric])

    def validate_old_password(self, old_password):
        user = self.context['user']
        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is not correct")
        return old_password
