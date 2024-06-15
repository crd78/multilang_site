# main/urls.py
from django.urls import path
from . import views
from .views import chatbot, set_language, article_list

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('chatbot/', chatbot, name='chatbot'),
    path('set_language/', set_language, name='set_language'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
]