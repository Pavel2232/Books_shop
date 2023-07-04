from user.models import Author
from rest_framework import serializers


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        author = Author.objects.create(**validated_data)

        author.set_password(validated_data['password'])
        author.save()

        return author
