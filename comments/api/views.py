from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated

from comments.api.serializers import (CommentDetailSerializer,
                                      CommentEditSerializer, CommentSerializer,
                                      create_comment_serializer, CommentCreateSerializer)
from comments.models import Comment
from posts.api.pagination import PostPageNumberPagination


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def get_serializer_context(self):
        context = super(CommentCreateAPIView, self).get_serializer_context()
        context['user'] = self.request.user
        return context


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'pk'


class CommentEditAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentEditSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # TODO: Fix removing comments
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'content',
        'user__first_name',
        'user__last_name',
        'user__username',
    ]
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = []
        query = self.request.GET.get('q')
        slug = self.request.GET.get('slug')
        type = self.request.GET.get('type')
        if slug:
            model_qs = ContentType.objects.filter(model=type)
            if not model_qs.exists():
                raise ValidationError("Invalid content type")

            SomeModel = model_qs.first().model_class()
            obj_qs = SomeModel.objects.filter(slug=slug)
            if obj_qs.exists():
                content_obj = obj_qs.first()
                queryset_list = Comment.objects.filter_by_instance(content_obj)
        else:
            queryset_list = Comment.objects.filter(id__gte=0)

        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(user__username__icontains=query)
            ).distinct()

        return queryset_list
