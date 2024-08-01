from django.urls import path
from teachers.views import TeachersList, TeacherCreateView, TeacherUpdateView

urlpatterns = [
    path('teachers/', TeachersList.as_view(), name='teacher'),
    path('add-teacher/', TeacherCreateView.as_view(), name= 'add_teacher'),
    path('teacher/<slug:slug>/edit/', TeacherUpdateView.as_view(), name='teacher_update')
]
