from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.overview, name='overview'),
    path('posts/', views.posts_management, name='posts_management'),
    path('users/', views.users_management, name='users_management'),
]
