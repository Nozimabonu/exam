from django.urls import path

from blogs.views import BlogsList, Detail, BlogCreateView, BlogUpdateView

urlpatterns = [
    path('blog-list/', BlogsList.as_view(), name='blog_list'),
    path('single/', Detail.as_view(), name='detail'),
    path('add-blog/', BlogCreateView. as_view(), name='add_blog'),
    path('update-blog/<int:pk>/', BlogUpdateView.as_view(), name='update_blog')
]
