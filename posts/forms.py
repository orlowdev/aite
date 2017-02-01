from django import forms

from .models import Post


# Post form builder
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publication_date",
        ]