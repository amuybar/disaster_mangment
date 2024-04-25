from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('create-topic/', views.create_topic, name='create_topic'),
    path('topic/<int:topic_id>/', views.view_topic, name='view_topic'),
]
