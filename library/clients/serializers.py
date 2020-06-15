from rest_framework.serializers import ModelSerializer

from .models import Client, Address, Rental
from books.serializers import BookSerializer


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ClientSerializer(ModelSerializer):
    address = AddressSerializer(read_only=False)

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        client = Client.objects.create(**validated_data)
        address, created = Address.objects.get_or_create(**address_data)
        client.address = address
        return client

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone', 'address']


class RentalSerializer(ModelSerializer):
    client = ClientSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = Rental
        fields = '__all__'
