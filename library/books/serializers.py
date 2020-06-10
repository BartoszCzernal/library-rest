from rest_framework.serializers import ModelSerializer

from .models import Book, Author, Category


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'date_of_release', 'authors', 'categories', 'on_loan_to']
