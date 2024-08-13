from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse
from blog.models import Blog, Category, Contact, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)

def blogs_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = blog
            new_comment.author = request.user
            new_comment.save()
            return redirect('blog_details', slug=blog.slug)
    else:
        comment_form = CommentForm()

    return render(request, "blog/blogs-details.html", {
        "blog": blog,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form
    })

@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.user == comment.author or request.user.is_staff:
        comment.delete()
        return redirect('blog_details', slug=comment.post.slug)
    else:
        return HttpResponse('Yorumu silmeye yetkiniz yok.', status=403)

def blogs_by_category(request, slug):
    a = get_object_or_404(Category, slug=slug)
    context = {
        "blogs": a.blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": a.name 
    }
    return render(request, "blog/blogs.html", context)


def hakkimda(request):
    return render(request, "blog/hakkimda.html")

def iletisim(request):
    if request.method == "POST":
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        return JsonResponse({"success": True})
    
    context = {
        'categories': Category.objects.all()
    }

    return render(request, 'blog/iletisim.html')


def search_api(request):
    query = request.GET.get('query', '')
    if query:
        results = Blog.objects.filter(title__icontains=query)[:5]
        results_data = [{'title': blog.title, 'url': blog.get_absolute_url()} for blog in results]
        return JsonResponse({'results': results_data})
    return JsonResponse({'results': []})
