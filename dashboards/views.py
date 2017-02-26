from django.shortcuts import render

from calendars.forms import CreateOrUpdateEventForm


def dashboard_main(request):
    event_form = CreateOrUpdateEventForm(request=request)
    return render(request, 'user_dashboard.html', {
        'event_form': event_form
    })
