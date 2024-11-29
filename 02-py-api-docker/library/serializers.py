from datetime import datetime
from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Book, Borrow


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "username", "email", "groups")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("url", "name")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("name", "author", "id", "is_available")

    is_available = serializers.SerializerMethodField()

    def get_is_available(self, book_object) -> bool:
        now = datetime.now()
        borrow = Borrow.objects.filter(
            book=book_object.id, start__lte=now, end__gte=now
        )
        return len(borrow) == 0


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ("start", "end", "book", "user", "id")
