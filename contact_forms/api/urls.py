from django.conf.urls import url

from contact_forms.api import views

urlpatterns = [
    url(r'^simple-contact/create/$', views.SimpleContactCreateAPIView.as_view(), name="simple-contact"),
    url(r'^bug-report/create/$', views.BugReportCreateAPIView.as_view(), name="bug-report"),
    url(r'^feedback/create/$', views.FeedbackCreateAPIView.as_view(), name="bug-report"),
]
