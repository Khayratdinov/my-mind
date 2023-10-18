from django.urls import path, include
from project.apps.users import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path(
        "register/",
        views.Register.as_view(),
        name="register",
    ),
    path("profile/", views.UserProfile.as_view(), name="profile"),
    path("edit_profile/", views.EditProfile.as_view(), name="edit_profile"),
]
