# Provides serialized Post creation
from rest_framework.serializers import ModelSerializer

from contact_forms.models import SimpleContact, BugReport, Feedback


class SimpleContactCreateSerializer(ModelSerializer):

    class Meta:
        model = SimpleContact
        fields = [
            "name",
            "email",
            "message",
        ]


class BugReportCreateSerializer(ModelSerializer):

    class Meta:
        model = BugReport
        fields = [
            "platform",
            "subject",
            "message",
        ]


class FeedbackCreateSerializer(ModelSerializer):

    class Meta:
        model = Feedback
        fields = [
            "subject",
            "message",
        ]
