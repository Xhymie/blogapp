from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Blog, Category, Contact, Comment
from .resources import BlogResource, CommentResource, CategoryResource, ContactResource
from django.utils.safestring import mark_safe 

class BlogAdmin(ImportExportModelAdmin):
    resource_class = BlogResource
    list_display = ("title", "is_active", "is_home", "slug", "selected_categories",)
    list_editable = ("is_active", "is_home")
    search_fields = ("title", "description")
    readonly_fields = ("slug",)
    list_filter = ("is_active", "is_home", "categories",)
    
    def selected_categories(self, obj):
        html = "<ul>"
        
        for category in obj.categories.all():
            html += "<li>" + category.name + "</li>"
        
        html += "</ul>"
        return mark_safe(html)

class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource

class ContactAdmin(ImportExportModelAdmin):
    resource_class = ContactResource

class CommentAdmin(ImportExportModelAdmin):
    resource_class = CommentResource

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
