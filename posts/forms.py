from django import forms
from .models import Post, Comment
from taggit.forms import TagField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded border'}),
            'content': forms.Textarea(attrs={'class': 'w-full'}),
            'category': forms.Select(attrs={'class': 'w-full px-4 py-2 rounded border'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'w-full px-4 py-2 rounded border', 'rows': 3}),
        }
