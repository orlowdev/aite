from django import forms

from calendars.models import Event, Calendar


class CreateOrUpdateEventForm(forms.ModelForm):
    title = forms.CharField()
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
        self.user = kwargs.pop('user', None)
        super(CreateOrUpdateEventForm, self).__init__(*args, **kwargs)

        self.fields['calendar'] = forms.ModelChoiceField(queryset=Calendar.objects.filter(user=self.user))
