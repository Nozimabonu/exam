from django.urls import path, include

from courses.views.views import Index, Courses, ContactFormView, AboutList, BaseInd, CDetail
from courses.views.authentication import register, CustomLoginView

urlpatterns = [
    # index
    path('home/', Index.as_view(), name='index'),
    path('', Courses.as_view(), name='course'),
    path('', BaseInd.as_view(), name='base'),
    path('course/<slug:slug>/', CDetail.as_view(), name='c_detail'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('about/', AboutList.as_view(), name='about'),

    # auth
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),

]
