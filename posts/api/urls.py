from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(), name="list"),
    url(r'^create/$', views.PostCreateAPIView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.PostDetailAPIView.as_view(), name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.PostUpdateAPIView.as_view(), name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.PostDeleteAPIView.as_view(), name="delete"),
]
