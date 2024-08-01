from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView

from courses.forms import ContactForm
from courses.models import Course, Category, Comment
from teachers.models import Teacher
from django.contrib import messages


class Index(ListView):
    model = Course
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['teachers'] = Teacher.objects.all()
        context['active_page'] = 'home'
        return context


class BaseInd(ListView):
    model = Category
    template_name = 'base/base.html'
    context_object_name = 'categories'


class Courses(ListView):
    model = Course
    template_name = 'courses/course.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['active_page'] = 'courses'
        return context


class CDetail(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context




class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'about/contact.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your message has been sent successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with your submission. Please correct the errors below.')
        return super().form_invalid(form)


class AboutList(ListView):
    model = Comment
    template_name = 'about/about.html'
    context_object_name = 'comments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'about'
        return context
