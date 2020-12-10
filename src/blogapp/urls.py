from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.article_list, name = 'list'),
    path('create/', views.article_create, name = 'create'),
    path('(?P<slug>[\w-]+)/', views.article_detail, name = 'detail'),
]
