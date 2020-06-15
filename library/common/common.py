from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField(null=True)

    class Meta:
        abstract = True


class PersonContact(Person):
    address = models.ForeignKey('clients.Address', on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    class Meta:
        abstract = True