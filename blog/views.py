from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView, TemplateView

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    queryset = Post.objects.filter(is_published=True)


class CategoryPostsView(ListView):
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'post_list'  

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'], is_published=True, category__is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] =  Category.objects.get(slug=self.kwargs['slug'])
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    pk_url_kwarg = 'id'

class AboutView(TemplateView):
    template_name = 'about.html'

class RulesView(TemplateView):
    template_name = 'rules.html'


