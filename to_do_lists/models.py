from django.db import models
from django.conf import settings
from django.urls import reverse

from calendars.models import Calendar, Event

TASK_PRIORITY_CHOICES = (
    ('lowest', 'Lowest'),
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ('highest', 'Highest'),
)


class Category(models.Model):
    name = models.CharField(max_length=128)
    icon = models.CharField(max_length=64)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

    def get_lists(self):
            return List.objects.filter(category=self)

    def get_absolute_url(self):
        return reverse("todo:category", kwargs={"pk": self.pk})


class List(models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=8)
    description = models.TextField()
    category = models.ForeignKey(to=Category)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    calendar = models.ForeignKey(to=Calendar, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("todo:list", kwargs={"pk": self.pk})

    def get_calendar_events(self):
            return Calendar.objects.filter(category=self)


class Task(models.Model):
    name = models.CharField(max_length=128)
    priority = models.CharField(max_length=16, choices=TASK_PRIORITY_CHOICES)
    complete = models.BooleanField(default=False)
    list = models.ForeignKey(to=List, null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    event = models.ForeignKey(to=Event, null=True, blank=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    def get_complete_tasks_count(self):
        return self.objects.filter(complete=True).count()

    def get_category(self):
        if self.list and self.list.category:
            return self.list.category

    def get_calendar(self):
        if self.list and self.list.calendar:
            return self.list.calendar

    def get_absolute_url(self):
        return reverse("todo:task", kwargs={"pk": self.pk})
