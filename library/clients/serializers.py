from rest_framework.serializers import ModelSerializer

from .models import Client, Address


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
