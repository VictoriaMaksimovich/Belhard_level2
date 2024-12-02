import datetime

from .models import Articles
from django.forms import ModelForm, TextInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'author', 'anons', 'full_text']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор статьи'}),
            'anons': TextInput(attrs={'class': 'form-control', 'placeholder': 'Анонс статьи'}),
            'full_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст статьи'}),
        }