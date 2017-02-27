from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from calendars.forms import CreateOrUpdateEventForm


@login_required
def dashboard_main(request):
    event_form = CreateOrUpdateEventForm(user=request.user)

    return render(request, 'user_dashboard.html', {
        'event_form': event_form
    })
