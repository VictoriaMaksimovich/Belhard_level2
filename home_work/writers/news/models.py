from django.db import models


class Articles(models.Model):
    author = models.CharField('Автор', max_length=20)
    title = models.CharField('Название', max_length=70)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
