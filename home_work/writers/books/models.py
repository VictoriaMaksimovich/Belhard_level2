from django.db import models
from django.urls import reverse

from users.models import User


class Style(models.Model):
    style_book = models.CharField('Жанр', max_length=20, default='Не указано')
    # slug = models.SlugField('URL', max_length=255, unique=True, db_index=True, help_text='только латинские')

    def __str__(self):
        return f'{self.style_book}'

    # def get_absolute_url(self):
    #     return reverse('style', kwargs={"style_slug": self.slug})
    #
    # def get_edit_url(self):
    #     return reverse('style_edit', kwargs={"id": self.pk})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Book(models.Model):
    title_book = models.CharField('Название книги', max_length=100, null=False, blank=False, unique=True)
    # slug = models.SlugField('URL', max_length=255, unique=True, db_index=True, help_text='только латинские')
    style_book = models.ForeignKey(to=Style, on_delete=models.PROTECT)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title_book}'

    # def get_absolute_url(self):
    #     return reverse('book', kwargs={"book_slug": self.slug})
    #
    # def get_edit_url(self):
    #     return reverse('book_edit', kwargs={"id": self.pk})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Chapter(models.Model):
    chapter = models.CharField('Название главы', max_length=70, null=False, blank=False)
    full_text = models.TextField('Текст главы', null=False, blank=False)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    # slug = models.SlugField('URL', max_length=255, unique=True, db_index=True, help_text='только латинские')
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.chapter}, {self.full_text}'

    # def get_absolute_url(self):
    #     return reverse('chapter', kwargs={"chapter_slug": self.slug})
    #
    # def get_edit_url(self):
    #     return reverse('chapter_edit', kwargs={"id": self.pk})

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'
