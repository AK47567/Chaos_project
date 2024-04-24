from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('generate_images/', views.generate_images, name='generate_images'),
]


















