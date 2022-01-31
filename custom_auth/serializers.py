from rest_framework import serializers

from users.models import User
from project.validators import CustomValidator


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
