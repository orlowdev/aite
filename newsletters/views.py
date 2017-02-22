from django.contrib import messages
from django.shortcuts import redirect

from newsletters.forms import SubscriptionForm


def subscription(request):

    form = SubscriptionForm(request.POST or None)

    if form.is_valid():
        messages.success(request, "Successfully saved", extra_tags="html_safe")

        form.save()

    return redirect('index')
