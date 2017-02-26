from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from calendars.models import Event, Calendar

events_url = HyperlinkedIdentityField(
    view_name='api-calendars:events',
    lookup_field='id',
)


class CalendarListSerializer(ModelSerializer):
    url = events_url

    class Meta:
        model = Calendar
        fields = [
            "url",
        ]

    def get_events(self, obj):
        c_qs = Event.objects.filter(calendar=obj)
        events = EventListSerializer(c_qs, many=True).data

        return events


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "start",
        ]
