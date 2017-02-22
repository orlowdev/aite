from django.shortcuts import render

from newsletters.forms import SubscriptionForm
from posts.models import Post


def index(request):
    posts = Post.objects.visible()[:3]
    form = SubscriptionForm(request.POST or None)

    return render(request, "main/index.html", {
        'posts': posts,
        'form': form,
    })
