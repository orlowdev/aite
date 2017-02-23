from django.conf.urls import url

from contact_forms.views import simple_contact_submission

urlpatterns = [
    url(r'^contact-us$', simple_contact_submission, name="simple"),
]
