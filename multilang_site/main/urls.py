# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    # Vous pouvez ajouter d'autres vues et chemins d'URL ici
]