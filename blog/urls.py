from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_author/', views.create_author, name='create_author'),
    path('create_category/', views.create_category, name='create_category'),
    path('search/', views.search, name='search'),
    path('post/<int:post_id>/', views.read_post, name='read_post'),
]
