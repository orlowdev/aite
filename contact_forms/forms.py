from django import forms

from contact_forms.models import SimpleContact


class SimpleContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form-contact-name',
                'placeholder': 'Your Name',
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'form-contact-email',
                'placeholder': 'Your Email',
            }
        )
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'form-contact-message',
                'placeholder': 'Your Message',
                'rows': 8,
            },
        )
    )

    class Meta:
        model = SimpleContact
        fields = [
            'name',
            'email',
            'message',
        ]
