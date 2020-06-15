from rest_framework.serializers import ModelSerializer

from .models import Client, Address, Rental


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class RentalSerializer(ModelSerializer):
    class Meta:
        model = Rental
        fields = "__all__"
