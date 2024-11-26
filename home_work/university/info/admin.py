from django.contrib import admin
from .models import Student, Teacher, Course


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'sex', 'active', 'short_name')
    search_fields = ('name', 'surname')
    list_filter = ('sex',)

    def short_name(self, obj):
        return f"{obj.surname} {obj.name[0]}."

    short_name.short_description = 'Короткое имя'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    search_fields = ('name', 'surname', 'subject')
    list_filter = ('subject',)


admin.site.register(Course)

