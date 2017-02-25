from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from calendars.api.serializers import EventListSerializer
from calendars.models import Event


class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'title',
    ]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Event.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')

        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)
            ).distinct()

        return queryset_list
