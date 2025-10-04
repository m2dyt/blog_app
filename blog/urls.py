from django.urls import path
from .views import PostListView, CategoryPostsView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', CategoryPostsView.as_view(), name='category_posts'),
]
