from rest_framework.generics import ListAPIView

from posts.models import Post


class PostListAPIView(ListAPIView):
    posts = Post.objects.all()

    # TODO: Add serializer