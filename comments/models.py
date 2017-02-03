from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CommentManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        object_id = instance.id
        queryset = super(CommentManager, self).filter(content_type=content_type, object_id=object_id)

        return queryset


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

    def __str__(self):
        return str(self.user.username)
