from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse, get_object_or_404
from blogs.models import Category, Blogs
from django.contrib.auth.decorators import login_required
from blog_app_2.forms import RegistrationForm, BlogPostForm
from django.template.defaultfilters import slugify
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_counts = Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()
    context = {
        'category_count':category_counts,
        'blogs_count':blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    # cats = Category.objects.all()
    
    return render(request, 'dashboard/categories.html')

def addCategory(request):
    return render(request, 'dashboard/add_categories.html' )

def posts(request):
    allposts = Blogs.objects.all()
    context = {
        'allposts':allposts
    }
    return render(request, 'dashboard/posts.html', context)

def addpost(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            post = form.save(commit=False)
            post.slug = slugify(title)
            post.author = request.user 
            post.save()
            print("success")
            return redirect(to='posts')
    else:
        print("error")
        # print(form.errors)
        form = BlogPostForm()
    context = {
        'form':form,
    }    
    return render(request,'dashboard/add_post.html', context)

def editpost(request,pk):
    post = get_object_or_404(Blogs, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.author = request.user 
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form':form,
        'post':post,
    }
    return render(request, 'dashboard/edit_post.html', context)

def deletepost(request,pk):
    post = get_object_or_404(Blogs,pk=pk)
    post.delete()
    return redirect('posts')