from django.db import models


# TODO: Add bug report and feedback models


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
