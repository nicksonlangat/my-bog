from django.urls import path
from . import views
from .views import (
    BlogIndex, BlogCreateView,BlogUpdateView,BlogDeleteView
)

urlpatterns = [
    path("", BlogIndex.as_view(), name="blog_index"),
    path("<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/edit/',
                     BlogUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/',
                     BlogDeleteView.as_view(), name='post_delete'),
    
]