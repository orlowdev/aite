from django.db.models import Q
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from calendars.api.serializers import EventListSerializer, CalendarListSerializer
from calendars.models import Event, Calendar


class CalendarListAPIView(ListAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarListSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        'name',
    ]

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            queryset_list = Calendar.objects.filter(user=self.request.user)
            query = self.request.GET.get('q')

            if query:
                queryset_list = queryset_list.filter(
                    Q(name__icontains=query)
                ).distinct()

            return queryset_list


class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        'title',
    ]

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            queryset_list = Event.objects.filter(calendar_id=self.kwargs['id'])
            query = self.request.GET.get('q')

            if query:
                queryset_list = queryset_list.filter(
                    Q(title__icontains=query)
                ).distinct()

            return queryset_list
