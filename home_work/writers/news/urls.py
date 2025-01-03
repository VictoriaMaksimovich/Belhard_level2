from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsView.as_view(), name='news_view'),
    path('my_news', views.user_news, name='user_news')
]
