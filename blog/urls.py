from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("blogs/<slug:slug>", views.blogs_details, name="blog_details"),
    path("hakkimda", views.hakkimda, name="hakkimda"),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('delete_comment/<int:id>/', views.delete_comment, name='delete_comment'),
    path('search-api/', views.search_api, name='search_api'),
]