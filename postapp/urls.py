from django.urls import path
from .views import getPosts, getPost, getPostsByTag, about

urlpatterns = [
    path('', getPosts, name='post_all'),
    path('detail/<int:pk>/', getPost, name='post_detail'),
    path('tag/<str:tagName>/', getPostsByTag, name='post_filter'),
    path('about/', about, name='about_me'),
]