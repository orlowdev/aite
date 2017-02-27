from django import forms

from calendars.models import Event, Calendar


class CreateOrUpdateEventForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'e.g. My birthday',
                                                          'id': 'titleField'}))
    start = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'e.g. 2017-02-28 07:24',
                                                                  'id': 'startTimeField'}))
    end = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control',
                                                                'placeholder': 'e.g. 2017-02-28 07:24',
                                                                'id': 'endTimeField'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Description',
                                                               'rows': 8,
                                                               'id': 'descriptionField'}))

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

        self.fields['calendar'] = forms.ModelChoiceField(queryset=Calendar.objects.filter(user=self.user),
                                                         widget=forms.Select(attrs={'class': 'form-control',
                                                                                    'id': 'calendarField'}))
