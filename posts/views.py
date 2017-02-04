from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from comments.forms import CommentForm
from comments.models import Comment

from . import options
from .forms import PostForm
from .models import Post
from .utils import get_read_time


# Post list view
def post_list(request):
    all_posts = Post.objects.visible()
    if request.user.is_staff or request.user.is_superuser:
        all_posts = Post.objects.all()

    """ Search presets """
    query = request.GET.get('q')
    if query:
        all_posts = all_posts.filter(Q(title__icontains=query) |
                                     Q(content__icontains=query) |
                                     Q(user__first_name__icontains=query) |
                                     Q(user__last_name__icontains=query) |
                                     Q(user__username__icontains=query)
                                     ).distinct()

    """ Paginator presets """
    paginator = Paginator(all_posts, options.BLOG_PAGINATION)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "list.html", {
        "posts": posts,
        "title": "List",
    })


# Post detail view
def post_detail(request, slug=None):

    post = get_object_or_404(Post, slug=slug)
    if post.draft or post.publication_date > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

    print(get_read_time(post.get_markdown()))

    """ Provide initial data to hidden fields of the form via 'initial' """
    form = CommentForm(request.POST or None, initial={
        'content_type': post.get_content_type,
        'object_id': post.id,
    })

    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content = form.cleaned_data.get("content")
        parent_object = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_queryset = Comment.objects.filter(id=parent_id)
            if parent_queryset.exists() and parent_queryset.count() == 1:
                parent_object = parent_queryset.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content,
            parent=parent_object,
        )

        """ Reload the same page to clean up the input field """
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    return render(request, "detail.html", {
        "post": post,
        "form": form,
    })


# Post create view
def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()

        """ Flash message """
        messages.success(request, "<a href='#'>Successfully created</a>", extra_tags=options.ALLOW_FLASH_REDIRECT)

        return HttpResponseRedirect(post.get_absolute_url())
    else:
        messages.error(request, "Not successfully created")

    return render(request, "create.html", {
        "form": form,
    })


# Post update view
def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    post = get_object_or_404(Post, slug=slug)

    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()

        """ Flash message """
        messages.success(request, "Successfully saved", extra_tags=options.ALLOW_FLASH_REDIRECT)

        return HttpResponseRedirect(post.get_absolute_url())
    else:
        """ Flash message """
        messages.error(request, "Saving failed")

    return render(request, "edit.html", {
        "post": post,
        "form": form,
    })


# Post delete view
def post_delete(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    return HttpResponse("<h1>Delete</h1>")
