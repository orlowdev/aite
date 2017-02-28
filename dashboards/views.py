from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from calendars.forms import CreateOrUpdateEventForm
from posts import options


@login_required
def dashboard_main(request):
    event_form = CreateOrUpdateEventForm(request.POST or None, user=request.user)
    if event_form.is_valid():
        event_form.save()
        messages.success(request, "<a href='#'>Successfully created</a>", extra_tags=options.ALLOW_FLASH_REDIRECT)

        return HttpResponseRedirect('dashboard')

    return render(request, 'user_dashboard.html', {
        'event_form': event_form
    })
