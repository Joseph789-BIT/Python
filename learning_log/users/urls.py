"""Defines URL patterns for users"""
from tempfile import template

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'  # This sets the application namespace

urlpatterns = [
    # Login page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
]