from django.shortcuts import render


def student_info(request):
    return render(request, 'info/student_info.html')

