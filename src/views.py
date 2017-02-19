# Main page view
from django.shortcuts import render

from posts.models import Post


def index(request):
    posts = Post.objects.visible()[:3]
    return render(request, "main/index.html", {
        'posts': posts,
    })
