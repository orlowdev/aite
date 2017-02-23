from django.contrib import admin

from contact_forms.models import BugReport, Feedback, SimpleContact


class BugReportAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'creation_date',
        'reply_sent',
    ]

    class Meta:
        model = BugReport


class FeedbackAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'creation_date',
        'fix_commit',
    ]

    class Meta:
        model = Feedback


class SimpleContactAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'creation_date',
    ]

    class Meta:
        model = SimpleContact

admin.site.register(BugReport)
admin.site.register(Feedback)
admin.site.register(SimpleContact, SimpleContactAdmin)
