from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '',
        }
        
class SearchForm(forms.Form):
    query = forms.CharField(label='Arama', max_length=100)