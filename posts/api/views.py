from rest_framework.generics import ListAPIView

from posts.api.serializers import PostSerializer
from posts.models import Post


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
