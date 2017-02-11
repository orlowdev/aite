"""
Serializer class for Post model
"""
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
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
    delete_url = post_delete_url
    url = post_detail_url

    html = SerializerMethodField()
    image = SerializerMethodField()
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "url",
            "user",
            "publication_date",
            "image",
            "title",
            "content",
            "html",
            "delete_url",
        ]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_user(self, obj):
        return str(obj.user.username)


# Provides serialized Post list data
class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "url",
            "publication_date",
            "title",
        ]

    def get_user(self, obj):
        return str(obj.user.username)
