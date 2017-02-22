from django.contrib import admin

from newsletters.forms import SubscriptionForm
from newsletters.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["__str__", "full_name", "date"]

    class Meta:
        model = Subscription

admin.site.register(Subscription, SubscriptionAdmin)
