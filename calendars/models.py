import datetime
from django.conf import settings
from django.db import models


class Event(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        default=1,
    )

    title = models.CharField(
        max_length=255,
    )

    start = models.DateTimeField()
    end = models.DateTimeField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return "{} at {}".format(self.title, datetime.datetime.strftime(self.start, "%Y-%m-%dT%X"))
