from django.contrib import admin
from project.apps.posts.models import Post, Category, Tag, PostComment


# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PostComment)
