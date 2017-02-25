# Provides serialized Post creation
from rest_framework.serializers import ModelSerializer

from contact_forms.models import SimpleContact


class SimpleContactCreateSerializer(ModelSerializer):

    class Meta:
        model = SimpleContact
        fields = [
            "name",
            "email",
            "message",
        ]
