from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from blogs.models import Author, Blog


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author
        fields = ('id', 'full_name', 'education')

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    resource_class = AuthorResource
    list_display = ('full_name', 'education')
    search_fields = ('full_name',)
    list_filter = ('education',)


class BlogResource(resources.ModelResource):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'slug', 'date_added', 'image')
        export_order = ('title', 'slug', 'date_added', 'image')


@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    resource_class = BlogResource
    list_display = ('title', 'slug', 'date_added', 'image')
    search_fields = ('title',)
    list_filter = ('date_added',)

