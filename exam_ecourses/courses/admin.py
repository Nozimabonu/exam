from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from courses.models import Course, Category


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('id', 'title')


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']


class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'number_of_students', 'price',
                  'duration', 'teachers', 'category', 'video', 'image')
        export_order = ('title', 'description', 'number_of_students', 'price',
                        'duration', 'teachers', 'category', 'video', 'image')


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource
    fields = ['title', 'description', 'number_of_students', 'price',
              'duration', 'teachers', 'category', 'video', 'image']
    list_display = ('title', 'slug', 'number_of_students', 'price')
    search_fields = ('title', 'teachers')
    list_filter = ('duration', 'price')
