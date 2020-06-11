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
    authors = AuthorSerializer(many=True, read_only=False)
    categories = CategorySerializer(many=True, read_only=False)

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        authors_data = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)
        for category_data in categories_data:
            category, created = Category.objects.get_or_create(**category_data)
            book.categories.add(category)
        for author_data in authors_data:
            author, created = Author.objects.get_or_create(**author_data)
            # get_or_create is case sensitive
            book.authors.add(author)
        return book

    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'date_of_release', 'authors', 'categories', 'on_loan_to']
