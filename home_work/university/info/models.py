from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Course(models.Model):
    langs = [
        ('py', 'Python'),
        ('js', 'JavaScript'),
        ('c', 'C++'),
        ('an', 'Android'),
    ]
    name = models.CharField(max_length=20, choices=langs)
    course_num = models.SmallIntegerField(
        default=1,
        verbose_name="Номер курса",
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    start_date = models.DateField('Начало курса')
    end_date = models.DateField('Окончание курса')
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return f"{self.name} - {self.course_num}"

    class Meta:
        unique_together = [['name', 'course_num']]
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['name', 'course_num']


class Student(models.Model):
    name = models.CharField('Имя', max_length=20, null=False, blank=False)
    surname = models.CharField('Фамилия', max_length=30, null=False, blank=False)
    sex = models.CharField('Пол', max_length=10, choices=[('m', 'Мужчина'), ('w', 'Женщина')])
    active = models.BooleanField('Активный')
    age = models.SmallIntegerField('Возраст', validators=[MinValueValidator(18), MaxValueValidator(120)])
    startDate = models.DateField('Дата поступления')
    course = models.ManyToManyField(to='Course', verbose_name='Посещаемые курсы')

    def __str__(self):
        return f"{self.name} {self.surname}"

    def get_absolute_url(self):
        return reverse('student', kwargs={"id": self.pk})

    class Meta:
        indexes = [models.Index(fields=['surname'])]
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        # unique_together = [['name', 'surname']]
        db_table = 'students'
        ordering = ["surname"]


class Mark(models.Model):
    mark = models.SmallIntegerField('Оценка', validators=[MinValueValidator(1), MaxValueValidator(10)])
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} - {self.mark}'

    class Meta:
        indexes = [models.Index(fields=['student'])]
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

