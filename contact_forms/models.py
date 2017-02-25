from django.conf import settings
from django.db import models


FEEDBACK_CHOICES = (
    ('suggestion', 'Suggestion'),
    ('complaint', 'Complaint'),
)

BUG_REPORT_CHOICES = (
    ('execution_error', 'Error during app execution'),
    ('spelling_mistake', 'Spelling mistake'),
    ('translation_mistake', 'Translation mistake'),
    ('authentication_problem', 'Problem with authentication/authorization'),
    ('other', 'Other'),
)

PLATFORM_CHOICES = (
    ('android', 'Android'),
    ('ios', 'iOS'),
    ('windows', 'Windows'),
    ('web', 'Web'),
)


class BugReport(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        default=1,
    )

    platform = models.CharField(
        max_length=32,
        choices=PLATFORM_CHOICES,
    )

    subject = models.CharField(
        max_length=32,
        help_text='Bug Type',
        choices=BUG_REPORT_CHOICES,
    )

    message = models.TextField(
        verbose_name='Message',
        help_text='Enter your message here',
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation Date',
        help_text='Date of bug report arrival',
    )

    fix_commit = models.CharField(
        max_length=64,
        verbose_name='Fixing Commit',
        help_text='Reference to a commit fixing the issue',
    )

    def __str__(self):
        return '{}: {} by {}'.format(self.platform, self.subject, self.user.username)


class Feedback(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        default=1,
    )

    subject = models.CharField(
        max_length=32,
        help_text='Subject',
        choices=FEEDBACK_CHOICES,
    )

    message = models.TextField(
        verbose_name='Message',
        help_text='Enter your message here',
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation Date',
        help_text='Date of feedback arrival'
    )

    def __str__(self):
        return '{} by {}'.format(self.subject, self.user.username)


class SimpleContact(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Name',
    )

    email = models.EmailField(
        verbose_name='Email',
    )

    message = models.TextField(
        verbose_name='Message',
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation Date',
        help_text='Date of message arrival',
        editable=False,
    )

    reply_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Reply Date',
        help_text='Date when reply was sent'
    )

    reply_sent = models.BooleanField(
        verbose_name='Reply Sent',
        default=False,
    )

    def __str__(self):
        return 'Message {} by {}'.format(self.id, self.email)
