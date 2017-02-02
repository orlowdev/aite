from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from markdown_deux import markdown

# Blog post model manager
class PostManager(models.Manager):
    def visible(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publication_date__lte=timezone.now())


# Upload location definition for user files
def upload_location(instance, filename):
    return "blog/posts/%s/%s" % (instance.id, filename)


# Blog post model
class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
    )
    title = models.CharField(
        max_length=128
    )
    slug = models.SlugField(
        unique=True
    )
    draft = models.BooleanField(
        default=False,
    )
    publication_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        null=True,
    )
    image = models.ImageField(
        upload_to=upload_location,
        width_field="width_field",
        height_field="height_field",
        null=True,
        blank=True,
    )
    height_field = models.IntegerField(
        default=0
    )
    width_field = models.IntegerField(
        default=0
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    """ Model manager injection
    'objects' is a conventional name yet it may be overriden
    In this case all references must be Post.'new_name'.* """
    objects = PostManager()

    def __str__(self):
        return self.title

    """ Return absolute url based on slug """
    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    """ Return markdown shrunk for post list view """
    def get_markdown(self):
        return mark_safe(markdown(self.content))

    class Meta:
        ordering = [
            "-created_at",
            "-updated_at",
            "title",
        ]


# Advanced slug builder
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-pk")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().pk)
        return create_slug(instance, new_slug=new_slug)
    return slug


# Pre-persist slug check
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)
