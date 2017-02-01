from django.contrib import admin

from .models import Post


# Post admin settings
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "updated_at", "created_at"]
    list_display_links = ["updated_at"]
    list_filter = ["updated_at", "created_at"]
    list_editable = ["title"]

    search_fields = ["title", "content"]

    class Meta:
        model = Post

# Admin logic pick up area
admin.site.register(Post, PostAdmin)
