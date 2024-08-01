from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from teachers.models import Teacher


class TeacherResource(resources.ModelResource):
    class Meta:
        model = Teacher
        fields = ('id', 'full_name', 'description', 'level', 'twitter_link', 'facebook_link', 'linkedin_link', 'image')
        export_order = ('full_name', 'description', 'level', 'twitter_link', 'facebook_link', 'linkedin_link', 'image')


@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    resource_class = TeacherResource
    fields = ['full_name', 'description', 'level', 'twitter_link', 'facebook_link', 'linkedin_link', 'image']
    list_display = ('full_name', 'slug', 'level', 'description')
    search_fields = ('full_name',)
    list_filter = ('level',)
