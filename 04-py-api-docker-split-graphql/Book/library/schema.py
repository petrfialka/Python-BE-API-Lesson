import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from .models import Book
from .serializers import BookSerializer


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "name", "author")


class BookMutation(SerializerMutation):
    class Meta:
        serializer_class = BookSerializer


class Query(graphene.ObjectType):
    get_books = graphene.List(BookType)

    def resolve_get_books(root, info):
        return Book.objects.all()


class Mutation(graphene.ObjectType):
    update_book = BookMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
