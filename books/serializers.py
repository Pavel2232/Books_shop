from rest_framework import serializers

from books.models import Book, Comment
from user.models import Author


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(
        read_only=True,
        required=False,
        slug_field='full_name',
        many=True
    )

    class Meta:
        model = Book
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        queryset=Author.objects.all(),
        slug_field='full_name'
    )
    book = serializers.SlugRelatedField(
        queryset=Book.objects.all(),
        slug_field='title'
    )

    class Meta:
        model = Comment
        fields = '__all__'
