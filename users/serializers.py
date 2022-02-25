from wsgiref import validate
from rest_framework import serializers

from .models import User,ShippingAddress

from project.validators import CustomValidator


class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['full_name','phone_number','email','address','province']
        #fields = '__all__'
        # extra_kwargs = {
        #     'user':{'required':True},
        # }
    
    # def create(self,validated_data):
    #     user_data = validated_data.pop('user')
    #     user = User.objects.create_user(**user_data)
    #     address = ShippingAddress.objects.create(user, **validated_data)
    #     return address


