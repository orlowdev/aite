from django import forms

from newsletters.models import Subscription


class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(
        label='Enter your email for the latest news',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'form-hero-email',
                'placeholder': 'Your email',
            }
        )
    )

    class Meta:
        model = Subscription
        fields = [
            'email',
        ]
