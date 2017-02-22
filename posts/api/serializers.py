from rest_framework.serializers import (HyperlinkedIdentityField,
                                        ModelSerializer, SerializerMethodField)

from accounts.api.serializers import UserDetailSerializer
from comments.api.serializers import CommentSerializer
from comments.models import Comment
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
    user = UserDetailSerializer(read_only=True)

    comments = SerializerMethodField()

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
            "comments",
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

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data

        return comments


# Provides serialized Post list data
class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "url",
            "publication_date",
            "title",
        ]
