from django.shortcuts import render

from contact_forms.forms import SimpleContactForm
from newsletters.forms import SubscriptionForm
from posts.models import Post


def index(request):
    posts = Post.objects.visible()[:3]
    subscription_form = SubscriptionForm()
    simple_contact_form = SimpleContactForm()

    return render(request, "main/index.html", {
        'posts': posts,
        'subscription_form': subscription_form,
        'simple_contact_form': simple_contact_form,
    })
