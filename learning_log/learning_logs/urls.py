from . import views
from django.urls import path, include

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('', include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')),
    path('new_topic/', views.new_topic, name='new_topic'),
]