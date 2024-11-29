from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from .models import Book, Borrow
from .serializers import (
    UserSerializer,
    GroupSerializer,
    BookSerializer,
    BorrowSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.order_by("id").all()
    serializer_class = BookSerializer


class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.order_by("id").all()
    serializer_class = BorrowSerializer
