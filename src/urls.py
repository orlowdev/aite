"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView

from rest_framework_jwt.views import obtain_jwt_token

from src.angular_js.views import AngularTemplateView

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^api/auth/token', obtain_jwt_token),
    url(r'^api/comments/', include("comments.api.urls", namespace="api-comments")),
    url(r'^api/contact-forms/', include("contact_forms.api.urls", namespace="api-contact-forms")),
    url(r'^api/calendar/', include("calendars.api.urls", namespace="api-calendars")),
    url(r'^api/posts/', include("posts.api.urls", namespace="api-posts")),
    url(r'^api/users/', include("accounts.api.urls", namespace="api-users")),

    url(r'^api/templates/(?P<item>[A-Za-z0-9\_\-\.\/]+)\.html$', AngularTemplateView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'', TemplateView.as_view(template_name='angular/main.html')),
]
