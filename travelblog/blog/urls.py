from django.urls import path
from . import views 
from .views import post_list, post_detail, about, contact

urlpatterns = [
    path('', views.index, name='home'),  # Головна сторінка
    path('about/', views.about, name='about'),  # Сторінка About
    path('contact/', views.contact, name='contact'),  # Сторінка Contact
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Сторінка детального перегляду поста
]