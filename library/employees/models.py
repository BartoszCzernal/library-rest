from django.db import models
from common.common import PersonContact


class Library(models.Model):
    address = models.ForeignKey('clients.Address', on_delete=models.PROTECT)


class Employee(PersonContact):
    library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True)


