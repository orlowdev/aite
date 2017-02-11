"""
Serializer class for Post model
"""
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
)

from posts.models import Post

post_detail_url = HyperlinkedIdentityField(
    view_name='api-posts:detail',
    lookup_field='slug',
)

post_delete_url = HyperlinkedIdentityField(
    view_name='api-posts:delete',
    lookup_field='slug',
)


# Provides serialized Post creation
class PostCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "publication_date",
            "title",
            "content",
            "draft",
        ]


# Provides serialized single Post data
class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    delete_url = post_delete_url

    class Meta:
        model = Post
        fields = [
            "id",
            "url",
            "publication_date",
            "title",
            "content",
            "delete_url",
        ]


# Provides serialized Post list data
class PostListSerializer(ModelSerializer):
    url = post_detail_url

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "url",
            "publication_date",
            "title",
        ]
