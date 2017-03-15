import os

from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import View


class AngularTemplateView(View):
    def get(self, request, item=None, *args, **kwargs):
        template_dir_path = settings.TEMPLATES[0]["DIRS"][0]
        final_path = os.path.join(template_dir_path, "angular", "app", item + ".html")

        try:
            html = open(final_path)
            return HttpResponse(html)
        except FileNotFoundError:
            raise Http404
