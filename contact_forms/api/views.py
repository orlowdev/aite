from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from contact_forms.api.serializers import SimpleContactCreateSerializer, BugReportCreateSerializer, \
    FeedbackCreateSerializer
from contact_forms.models import SimpleContact, BugReport, Feedback


class SimpleContactCreateAPIView(CreateAPIView):
    queryset = SimpleContact.objects.all()
    serializer_class = SimpleContactCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class BugReportCreateAPIView(CreateAPIView):
    queryset = BugReport.objects.all()
    serializer_class = BugReportCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeedbackCreateAPIView(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
