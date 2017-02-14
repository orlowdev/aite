from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

from accounts.api.serializers import UserDetailSerializer
from comments.models import Comment

User = get_user_model()


def create_comment_serializer(model_type='post', slug=None, parent_id=None, user=None):
    class CommentCreateSerializer(ModelSerializer):
        class Meta:
            model = Comment
            fields = [
                "id",
                "user",
                "created_at",
                "content",
            ]

        def __init__(self, *args, **kwargs):
            self.model_type = model_type
            self.slug = slug
            self.parent_obj = None
            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    self.parent_obj = parent_qs.first()
            return super(CommentCreateSerializer, self).__init__(*args, **kwargs)

        def validate(self, data):
            model_type = self.model_type
            model_qs = ContentType.objects.filter(model=model_type)
            if not model_qs.exists() or model_qs.count() != 1:
                raise ValidationError("Invalid content type")

            SomeModel = model_qs.first().model_class()
            obj_qs = SomeModel.objects.filter(slug=slug)
            if not obj_qs.exists() or obj_qs.count() != 1:
                raise ValidationError("Content type and slug do not match")

            return data

        def create(self, validated_data):
            content = validated_data.get("content")
            if user:
                main_user = user
            else:
                main_user = User.objects.all().first()
            model_type = self.model_type
            slug = self.slug
            parent_obj = self.parent_obj
            comment = Comment.objects.create_by_model_type(
                model_type, slug, content, main_user, parent_obj
            )

            return comment

    return CommentCreateSerializer


class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
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
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "created_at",
            "content",
        ]


class CommentDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    replies = SerializerMethodField()
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
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


class CommentEditSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "created_at",
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
