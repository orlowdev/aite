from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.mixins import (
    DestroyModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import (
    IsAuthenticated,
)

from posts.api.pagination import (
    PostPageNumberPagination,
)

from comments.models import Comment
from accounts.api.serializers import (
    UserCreateSerializer,
)

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
