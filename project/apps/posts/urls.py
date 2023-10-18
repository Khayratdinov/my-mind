from django.urls import path
from project.apps.posts.views import (
    PostsListView,
    PostDetailView,
)

urlpatterns = [
    path("", PostsListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]
