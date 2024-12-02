import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from .models import Borrow
from .serializers import BorrowSerializer


class BorrowType(DjangoObjectType):
    class Meta:
        model = Borrow
        fields = ("start", "end", "book", "user", "id")


class BorrowMutation(SerializerMutation):
    class Meta:
        serializer_class = BorrowSerializer


class Query(graphene.ObjectType):
    get_borrows = graphene.List(BorrowType)

    def resolve_get_borrows(root, info):
        return Borrow.objects.all()


class Mutation(graphene.ObjectType):
    update_book = BorrowMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
