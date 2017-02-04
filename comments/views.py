from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Comment
from .forms import CommentForm


def comment_thread(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    initial_data = {
        "content_type": comment.content_type,
        "object_id": comment.object_id,
    }

    form = CommentForm(request.POST or None, initial=initial_data)

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

    return render(request, "thread.html", {
        "comment": comment,
        "form": form,
    })


def comment_delete(request):
    pass
