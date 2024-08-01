from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from courses.models import Category
from teachers.forms import TeacherForm
from teachers.models import Teacher


class TeachersList(ListView):
    model = Teacher
    template_name = 'teachers/teacher.html'
    context_object_name = 'teachers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'teachers'
        return context



class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher')


class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher')