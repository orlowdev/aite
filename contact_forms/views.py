from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

from contact_forms.forms import SimpleContactForm


def simple_contact_submission(request):

    form = SimpleContactForm(request.POST or None)

    if form.is_valid():
        messages.success(request, "Thank you! We will contact you shortly via email you provided.",
                         extra_tags="html_safe")

        form.save()
        subject = 'Contact form applied'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = '{} contacted via simple form'.format(
            form.cleaned_data.get('email'),
        )
        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=False
        )

    return redirect('index')
