from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<slug>/', views.post_detail, name='post_detail'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<slug>/edit/', views.post_edit, name='post_edit'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<slug>/', views.category_details, name='category_details'),
    path('tags/',views.tag_list,name='tag_list'),
    path('posts/', views.show_filtered_posts, name='show_filtered_posts'),
    path('tags/<slug>/', views.tag_details, name='tag_details'),
    
]