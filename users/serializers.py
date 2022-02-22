from rest_framework import serializers

from .models import User,ShippingAddress
from project.validators import CustomValidator


class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['full_name','phone_number','email','address','province']
        #fields = '__all__'