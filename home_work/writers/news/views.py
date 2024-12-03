from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required


def news_home(request):
    news = Article.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsView(DetailView):
    model = Article
    template_name = 'news/news_view.html'
    context_object_name = 'article'


@login_required
def user_news(request):
    news = Article.objects.filter(user=request.user)
    return render(request, 'user_news.html', {'news': news})


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)
