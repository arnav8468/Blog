from django.urls import path
from . import views

app_name = 'ai'

urlpatterns = [
    path('generate/', views.ai_generate, name='ai_generate'),
    path('summary/<int:post_id>/', views.ai_summary, name='ai_summary'),
    path('suggest-tags/<int:post_id>/', views.ai_suggest_tags, name='ai_suggest_tags'),
    path('improve/<int:post_id>/', views.ai_improve, name='ai_improve'),
]
