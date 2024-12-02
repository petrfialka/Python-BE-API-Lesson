from rest_framework import serializers
from graphene_django import DjangoObjectType
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("name", "author", "id")
