from django import forms
from courses.models import Course, Category, User
from teachers.models import Teacher
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class CourseForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}), )
    teachers = forms.ModelChoiceField(
        queryset=Teacher.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}), )

    class Meta:
        model = Course
        fields = ('title', 'description', 'number_of_students', 'price',
                  'duration', 'teachers', 'category', 'video',)




class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'birth_of_date', 'email')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput)


from django import forms
from courses.models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
