from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    content = models.TextField()
    image = models.ImageField(upload_to="post")
    status = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts"
    )
    tag = models.ManyToManyField(Tag, related_name="posts")
    bookmark = models.ManyToManyField(User, related_name="post_bookmark")
    likes = models.ManyToManyField(User, related_name="post_likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent_comment = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.CASCADE, related_name="replies"
    )
    message = models.TextField()
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.get_username()}"

    @property
    def children(self):
        return PostComment.objects.filter(parent_comment=self).reverse()

    @property
    def is_parent(self):
        if self.parent_comment is None:
            return True
        return False
