from django.shortcuts import render, redirect
from .forms import BookForm, ChapterForm, StyleForm
from .models import Book, Style, Chapter


def style_view(request):
    if request.method == 'POST':
        form = StyleForm(request.POST)
        if form.is_valid():
            selected_style = form.cleaned_data['style_choice']
            new_style = form.cleaned_data['new_style']

            if new_style:
                Style.objects.create(style_book=new_style)
                return redirect('book_view')

            if selected_style:
                return redirect('book_view')

    else:
        form = StyleForm()

    return render(request, 'style_view.html', {'form': form})


def book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            selected_book = form.cleaned_data['book_choice']
            new_book = form.cleaned_data['new_book']

            if new_book:
                Book.objects.create(title_book=new_book)
                return redirect('chapter_add')

            if selected_book:
                chapters = selected_book.objects.get.all()
                return render(request, 'chapter_view.html',
                              {'chapters': chapters, 'book': selected_book})

    else:
        form = BookForm()

    return render(request, 'book_view.html', {'form': form})


def chapter_add(request):
    error = ''
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_home')
        else:
            error = 'Форма заполнена неверно'

    else:
        form = BookForm()

        data = {
            'form': form,
            'error': error
        }

        return render(request, 'books/chapter_add.html', data)

