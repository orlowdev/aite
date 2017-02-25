from django.contrib import admin

from calendars.models import Event, Calendar

admin.site.register(Calendar)
admin.site.register(Event)
