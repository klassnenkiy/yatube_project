from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # Страницы сообществ (назовём их groups)
    path('group/<slug:slug>/', views.group_posts),
] 