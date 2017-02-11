"""
Serializer class for Post model
"""
from rest_framework.serializers import ModelSerializer

from posts.models import Post


# Provides serialized Post list data
class PostListSerializer(ModelSerializer):
    """
    Returns primary key, date of publication, title, content and slug
    """

    class Meta:
        model = Post
        fields = [
            "id",
            "publication_date",
            "slug",
            "title",
        ]


# Provides serialized single Post data
class PostDetailSerializer(ModelSerializer):
    """
    Returns primary key, date of publication, title, content and slug
    """

    class Meta:
        model = Post
        fields = [
            "id",
            "publication_date",
            "slug",
            "title",
            "content",
        ]
