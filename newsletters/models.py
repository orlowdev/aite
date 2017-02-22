from django.db import models


class Subscription(models.Model):
    email = models.EmailField(
        verbose_name='Email',
        help_text='Email of the subscriber to send messages to',
    )
    full_name = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='Full Name',
        help_text='Used to refer to the subscriber in the message',
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of Subscription',
        editable=False,
    )

    def __str__(self):
        return self.email
