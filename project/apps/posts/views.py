from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

# ============================================================================ #

from project.apps.posts.forms import CommentForm
from project.apps.posts.models import Post, PostComment

# ============================================================================ #


# =============================== POSTSLISTVIEW ============================== #


class PostsListView(View):
    def get(self, request):
        posts = Post.objects.filter(status=True).order_by("-created_at")
        paginator = Paginator(posts, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "index.html", {"page_obj": page_obj})


# ============================== POSTDETAILVIEW ============================== #


class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, "post_detail.html", {"post": post})
