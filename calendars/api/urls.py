from django.conf.urls import url

from calendars.api import views

urlpatterns = [
    url(r'^list/$', views.CalendarListAPIView.as_view(), name="list"),
    url(r'^(?P<id>\d+)/events/$', views.EventListAPIView.as_view(), name="events"),
    url(r'^(?P<id>\d+)/events/create/$', views.EventCreateAPIView.as_view(), name="add-event"),
    url(r'^(?P<calendar_id>\d+)/events/(?P<id>\d+)/edit/$', views.EventUpdateAPIView.as_view(), name="edit-event"),
]
