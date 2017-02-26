from django.conf.urls import url

from calendars.api import views

urlpatterns = [
    url(r'^list/$', views.CalendarListAPIView.as_view(), name="list"),
    url(r'^(?P<id>\d+)/events/$', views.EventListAPIView.as_view(), name="events"),
]
