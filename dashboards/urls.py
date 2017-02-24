from django.conf.urls import url

from dashboards.views import dashboard_main

urlpatterns = [
    url(r'^$', dashboard_main, name="main"),
]
