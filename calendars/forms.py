from django import forms

from calendars.models import Event, Calendar


class CreateOrUpdateEventForm(forms.ModelForm):
    title = forms.CharField()
    calendar = forms.ModelChoiceField(
        queryset=Calendar.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Calendar',
            }
        )
    )
    start = forms.DateTimeField()

    end = forms.DateTimeField()

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Description',
                'rows': 8,
            },
        )
    )

    class Meta:
        model = Event
        fields = [
            'title',
            'calendar',
            'start',
            'end',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateOrUpdateEventForm, self).__init__(*args, **kwargs)