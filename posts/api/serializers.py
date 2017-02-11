"""
Serializer class for Post model
"""
from rest_framework.serializers import ModelSerializer

from posts.models import Post


# Provides serialized Post data
class PostSerializer(ModelSerializer):
    """
    Returns primary key, date of publication, title, content and slug
    """

    class Meta:
        model = Post
        fields = [
            "pk",
            "publication_date",
            "slug",
            "title",
            "content",
        ]
