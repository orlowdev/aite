from django.conf.urls import url

from .views import (
    CommentCreateAPIView,
    CommentDetailAPIView,
    CommentListAPIView,
)

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name="list"),
    url(r'^create/$', CommentCreateAPIView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name="thread"),
    # url(r'^(?P<pk>\d+)/delete/$', comment_delete, name="delete"),
]
