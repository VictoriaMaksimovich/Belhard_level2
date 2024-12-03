from django.db import models
from users.models import User


class Article(models.Model):
    title_article = models.CharField('Название', max_length=70)
    anons_article = models.CharField('Анонс', max_length=250)
    full_text_art = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title_article}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
