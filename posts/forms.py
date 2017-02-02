from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post


# Post form builder
class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget)
    publication_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publication_date",
        ]