from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime, timedelta


class Address(models.Model):
    city = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=20)

    def __repr__(self):
        return "Address(city='{}', street='{}', house_number='{}')".format(self.city, self.street, self.house_number)

    def __str__(self):
        return "{}, {}, {}".format(self.city, self.street, self.house_number)


class Client(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40)
    address = models.ForeignKey(Address, on_delete=models.SET_DEFAULT, default=None)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    date_of_birth = models.DateField()

    def __repr__(self):
        return "Client(first_name='{}', last_name='{}')".format(self.first_name, self.last_name)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Rental(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    book = models.ForeignKey('books.Book', on_delete=models.PROTECT)
    date_rental = models.DateField(auto_now_add=True)
    date_expected_return = models.DateField(default=datetime.now().date() + timedelta(days=30))
    date_return = models.DateField(null=True)

    def __repr__(self):
        return "Rental(client='{}', book='{}')".format(self.client.first_name + ' ' + self.client.last_name,
                                                       self.book.title)



