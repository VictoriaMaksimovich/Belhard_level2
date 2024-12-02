from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_view, name='book_view'),
    path('chapter_add', views.chapter_add, name='chapter_add'),
    path('style', views.style_view, name='style_view'),
]
