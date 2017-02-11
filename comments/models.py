from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


# Comment Manager
class CommentManager(models.Manager):

    # Override default query to ignore objects with parent
    def all(self):
        return super(CommentManager, self).filter(parent=None)

    # Filter by content type (e.g. Post) and its ID
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        object_id = instance.id
        return super(CommentManager, self).filter(content_type=content_type, object_id=object_id).filter(parent=None)


# Comment Model
class Comment(models.Model):

    # Set default user to admin (protected as comments are restricted for anons)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        verbose_name='Author',
        help_text='Author of the comment.',
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name='Content Type',
        help_text='Type of content to which this comment relates (e.g. Post, Message)',
    )

    object_id = models.PositiveIntegerField(
        verbose_name='Content ID',
        help_text='ID of the object to which this comment relates',
    )

    content_object = GenericForeignKey(
        'content_type',
        'object_id',
    )

    parent = models.ForeignKey(
        "self",
        verbose_name="Parent Comment",
        help_text="Parent comment if current comment is a reply",
        null=True,
        blank=True,
    )

    content = models.TextField(
        verbose_name='Content',
        help_text='Contents of the comment (Markdown aware)',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation Date',
        help_text='Date of creation (is set automatically)',
    )

    # Manager call
    objects = CommentManager()

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse("comments:thread", kwargs={"pk": self.pk})

    def children(self):  # replies
        return Comment.objects.filter(parent=self)

    def get_delete_url(self):
        return reverse("comments:delete", kwargs={"pk": self.pk})

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
