from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

from comments.models import Comment


class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "content_type",
            "object_id",
            "created_at",
            "parent",
            "reply_count",
            "content",
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0


class CommentChildSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            "id",
            "created_at",
            "content",
        ]


class CommentDetailSerializer(ModelSerializer):
    replies = SerializerMethodField()
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "content_type",
            "object_id",
            "created_at",
            "content",
            "reply_count",
            "replies",
        ]

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(
                obj.children(),
                many=True).data
        return None

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0
