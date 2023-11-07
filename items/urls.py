from django.urls import path, include

urlpatterns = [
    path("api/v1/", include("items.api.v1.urls"))
]