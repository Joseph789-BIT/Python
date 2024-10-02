"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    path('^$', views.index, name='index'),
]