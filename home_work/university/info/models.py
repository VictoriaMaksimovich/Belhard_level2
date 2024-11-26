from django.db import models


class Course(models.Model):
    number = models.CharField('Курс', max_length=1, choices=[1, 2, 3, 4, 5])

    def __str__(self):
        return f"{self.number}"


class Student(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=30)
    sex = models.CharField(max_length=10, choices=[('m', 'Мужчина'), ('w', 'Женщина')])
    active = models.BooleanField()
    startDate = models.DateField(null=True)
    student = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Teacher(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=30)
    subject = models.CharField('Предмет', max_length=20, choices=['Информатика', 'Математика',
                                                                  'Физика', 'Химия', 'Биология', 'Физкультура'])
    student = models.ManyToManyField(Student, through="Student")

    def __str__(self):
        return f"{self.name} {self.surname}"



