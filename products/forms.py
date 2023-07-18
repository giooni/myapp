from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    txt = forms.CharField(widget = forms.Textarea(attrs={
        'rows': '4',
    }))
    class Meta:
        model = Comment
        fields = ['txt']