from django.urls import path
from project.apps.posts.views import (
    PostsListView,
    PostDetailView,
    LikeView,
)

urlpatterns = [
    path("", PostsListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("like/<int:pk>/", LikeView.as_view(), name="like_post"),
]
