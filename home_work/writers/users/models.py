from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField('Имя', max_length=20, null=False, blank=False)
    login = models.CharField('Логин', max_length=20, null=False, blank=False, unique=True)
    password = models.CharField('Пароль', max_length=20, null=False, blank=False, unique=True)
    photo = models.ImageField('Фото', upload_to=r'photos/%Y/%m/%d', blank=True)
    # поле для формирования уникальной ссылки из символов а не id
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True, help_text='только латинские')

    def __str__(self):
        return f'{self.login}'

    def get_absolute_url(self):
        return reverse('user', kwargs={'name_slug': self.slug})

    def get_edit_url(self):
        return reverse('user_edit', kwargs={'id': self.pk})

    class Meta:
        indexes = [models.Index(fields=['login'])]
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        unique_together = [['name', 'login']]
        db_table = 'users'
        ordering = ['login']
