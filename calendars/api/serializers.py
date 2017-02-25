from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from calendars.models import Event, Calendar


class CalendarListSerializer(ModelSerializer):
    events = SerializerMethodField()

    class Meta:
        model = Calendar
        fields = [
            "id",
            "name",
            "events",
        ]

    def get_events(self, obj):
        c_qs = Event.objects.filter(calendar=obj)
        comments = EventListSerializer(c_qs, many=True).data

        return comments


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "start",
            "calendar",
        ]
