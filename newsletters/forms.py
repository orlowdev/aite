from django import forms

from newsletters.models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = [
            'email',
            'full_name',
        ]
