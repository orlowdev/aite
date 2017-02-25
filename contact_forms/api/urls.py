from django.conf.urls import url

from contact_forms.api import views

urlpatterns = [
    url(r'^create/$', views.SimpleContactCreateAPIView.as_view(), name="create"),
]
