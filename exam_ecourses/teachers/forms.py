from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name', 'description', 'level', 'twitter_link', 'facebook_link', 'linkedin_link', 'image']
