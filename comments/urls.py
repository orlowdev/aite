from django.conf.urls import url

from .views import comment_delete, comment_thread

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', comment_thread, name="thread"),
    url(r'^(?P<pk>\d+)/delete/$', comment_delete, name="delete"),
]
