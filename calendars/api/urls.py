from django.conf.urls import url

from calendars.api import views

urlpatterns = [
    url(r'^list/$', views.EventListAPIView.as_view(), name="list"),
]
