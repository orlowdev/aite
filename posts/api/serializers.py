"""
Serializer class for Post model
"""
from rest_framework.serializers import ModelSerializer

from posts.models import Post


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

    class Meta:
        model = Post
        fields = [
            "id",
            "publication_date",
            "slug",
            "title",
            "content",
        ]


# Provides serialized Post list data
class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "publication_date",
            "slug",
            "title",
        ]
