from django.contrib import admin
from .models import Student, Course, Mark


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('langs', 'course_num', 'start_date', 'end_date', 'description')
    search_fields = ('langs', 'course_num', 'start_date')


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'sex', 'active', 'short_name', 'startDate')
    search_fields = ('name', 'surname', 'startDate')
    list_filter = ('sex', 'startDate')

    def short_name(self, obj):
        return f"{obj.surname} {obj.name[0]}."

    short_name.short_description = 'Короткое имя'


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'mark')
    search_fields = ('student', 'mark')
    list_filter = ('student',)




