from rest_framework.serializers import ModelSerializer

from calendars.models import Event


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            "id",
            "user",
            "title",
            "start",
        ]
