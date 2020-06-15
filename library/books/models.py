from django.db import models
from isbn_field import ISBNField


class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40)

    def __repr__(self):
        return "Author(first_name='{}', last_name='{}')".format(self.first_name, self.last_name)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __repr__(self):
        return "Category(name='{}')".format(self.name)

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn = ISBNField()
    title = models.CharField(max_length=100)
    date_of_release = models.DateField(null=True, blank=True)
    authors = models.ManyToManyField(Author, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    on_loan_to = models.ForeignKey('clients.Client', on_delete=models.SET_NULL, null=True, blank=True)

    # owned_by : ForeignKey Library

    def __repr__(self):
        return "Book(isbn='{}', title='{}')".format(self.isbn, self.title)

    def __str__(self):
        return '{} - {}'.format(self.title, self.date_of_release)
