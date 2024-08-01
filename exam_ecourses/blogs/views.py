from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView

from blogs.forms import BlogForm
from blogs.models import Blog
from courses.models import Category


class BlogsList(ListView):
    model = Blog
    template_name = 'blogs/blog.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        num_of_categories = categories.count()

        context.update({
            'categories': categories,
            'num_of_categories': num_of_categories,
            'active_page': 'blog'
        })
        return context


class Detail(ListView):
    model = Blog
    template_name = 'blogs/detail.html'
    context_object_name = 'blogs'  # or whatever context name you need for single blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        num_of_categories = categories.count()

        context.update({
            'categories': categories,
            'num_of_categories': num_of_categories,
            'active_page': 'blog'
        })
        return context


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name ='blogs/add_blog.html'
    success_url = reverse_lazy('blog_list')




class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blogs/update_blog.html'
    success_url = reverse_lazy('blog_list')




def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)

        if Blog.objects.filter(slug=self.slug).exists():
            i = 1
            while True:
                new_slug = f"{self.slug}-{i}"
                if not Blog.objects.filter(slug=new_slug).exists():
                    self.slug = new_slug
                    break
                i += 1

    super(Blog, self).save(*args, **kwargs)