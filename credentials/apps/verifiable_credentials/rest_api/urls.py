"""Root API URLs for verifiable_credentials."""
from django.urls import include, re_path


urlpatterns = [
    re_path(r"^v1/", include(("credentials.apps.verifiable_credentials.rest_api.v1.urls", "v1"), namespace="v1")),
]
