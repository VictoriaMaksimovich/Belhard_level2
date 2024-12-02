from .models import Book, Style, Chapter
from django import forms

# style = ('Детектив', 'Фантастика', 'Фэнтези', 'Любовный роман', 'Приключения', 'Фанфик', 'Другое')


class StyleForm(forms.Form):
    style_choice = forms.ModelChoiceField(queryset=Style.objects.all(), required=False, label='Определите жанр')
    new_style = forms.CharField(max_length=20, required=False, label='Или введите новый вариант')


class BookForm(forms.Form):
    book_choice = forms.ModelChoiceField(queryset=Book.objects.all(), required=False, label='Выберите книгу')
    new_book = forms.CharField(max_length=50, required=False, label='Или введите новый вариант')


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'
