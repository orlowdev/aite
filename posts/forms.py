from django import forms
from pagedown.widgets import PagedownWidget

from .models import Post


# Post form builder
class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    publication_date = forms.DateField()

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publication_date",
        ]
