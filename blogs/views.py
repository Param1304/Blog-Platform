from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Blogs, Category
# Create your views here.
def posts_by_category(request, category_id):
    posts = Blogs.objects.filter(status='published', category = category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'category':category
    }
    return render(request,'posts_by_category.html', context)
    # return HttpResponse("posts by category", category_id)
    
def blogs(request,slug):
    single_post = get_object_or_404(Blogs, slug=slug, status='published', )
    context = {
        'post':single_post
    }
    return render(request, 'blogs.html', context)
    # return HttpResponse("single blog page")
# def register():
    