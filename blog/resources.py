from import_export import resources
from .models import Blog, Comment, Category, Contact

class BlogResource(resources.ModelResource):
    class Meta:
        model = Blog

class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
