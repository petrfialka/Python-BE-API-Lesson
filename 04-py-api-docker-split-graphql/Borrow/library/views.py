from datetime import datetime
from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from .models import Borrow
from .serializers import (
    UserSerializer,
    GroupSerializer,
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


class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.order_by("id").all()
    serializer_class = BorrowSerializer

    @extend_schema(
        responses={
            200: OpenApiResponse(
                response={
                    "type": "object",
                    "properties": {
                        "book_avaliable": {
                            "type": "bool",
                        }
                    },
                    "example": {
                        "book_avaliable": True,
                    },
                }
            )
        },
        parameters=[
            OpenApiParameter(
                name="book_id",
                required=True,
                type=int,
                location=OpenApiParameter.PATH,
            )
        ],
    )
    @action(
        detail=False,
        methods=["GET"],
        url_path="is_book_avaliable/(?P<book_id>[^/.]+)",
    )
    def is_book_avaliable(self, request, pk=None, book_id: int = None):
        now = datetime.now()
        borrows = Borrow.objects.filter(book=book_id, start__lte=now, end__gte=now)
        return Response({"book_avaliable": len(borrows) == 0})
