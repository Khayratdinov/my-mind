from django.urls import path, include
from project.apps.users import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path(
        "register/",
        views.Register.as_view(),
        name="register",
    ),
]
