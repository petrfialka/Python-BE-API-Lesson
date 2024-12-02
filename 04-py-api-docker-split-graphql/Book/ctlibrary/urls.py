from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from library.views import BookViewSet


router = routers.DefaultRouter()
router.register(r"books", BookViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/swagger",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
