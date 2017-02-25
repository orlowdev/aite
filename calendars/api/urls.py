from django.conf.urls import url

from calendars.api import views

urlpatterns = [
    url(r'^list/$', views.CalendarListAPIView.as_view(), name="list"),
]
