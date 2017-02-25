from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from contact_forms.api.serializers import SimpleContactCreateSerializer
from contact_forms.models import SimpleContact


class SimpleContactCreateAPIView(CreateAPIView):
    queryset = SimpleContact.objects.all()
    serializer_class = SimpleContactCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()
