import datetime
from django.conf import settings
from django.db import models


class Calendar(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        default=1,
    )
    name = models.CharField(
        max_length=255,
    )
    color = models.CharField(
        max_length=10,
    )

    def __str__(self):
        return self.name

    def get_events(self):
        return Event.objects.filter(calendar=self)


class Event(models.Model):
    title = models.CharField(
        max_length=255,
    )
    start = models.DateTimeField()
    end = models.DateTimeField(
        blank=True,
        null=True,
    )
    calendar = models.ForeignKey(
        to=Calendar,
        null=True,
        blank=True,
    )
    description = models.TextField()

    def __str__(self):
        return "{} at {}".format(self.title, datetime.datetime.strftime(self.start, "%Y-%m-%dT%X"))
