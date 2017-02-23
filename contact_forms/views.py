from django.contrib import messages
from django.shortcuts import redirect

from contact_forms.forms import SimpleContactForm


def simple_contact_submission(request):

    form = SimpleContactForm(request.POST or None)

    if form.is_valid():
        messages.success(request, "Thank you! We will contact you shortly via email you provided.",
                         extra_tags="html_safe")

        form.save()

    return redirect('index')
