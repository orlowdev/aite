from django.contrib import admin

from contact_forms.models import SimpleContact


class SimpleContactAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'creation_date',
        'reply_sent',
    ]

    class Meta:
        model = SimpleContact

admin.site.register(SimpleContact, SimpleContactAdmin)
