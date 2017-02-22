from django.conf.urls import url

from newsletters.views import subscription

urlpatterns = [
    url(r'^$', subscription, name="subscription"),
]
