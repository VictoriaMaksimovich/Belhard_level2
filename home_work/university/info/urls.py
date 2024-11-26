from django.urls import path
from . import views


urlpatterns = [
    path('', views.student_info, name='student_info'),
]