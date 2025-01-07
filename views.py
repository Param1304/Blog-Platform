from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from blogs.models import Category, Blogs
from django.contrib import auth
from .forms import RegistrationForm, BlogPostForm
def home(request):
    categories= Category.objects.all()
    featured_post = Blogs.objects.filter(is_featured=True)
    post = Blogs.objects.filter(is_featured=False, status='published')
    # print(post)
    # print(featured_post)
    context = {
        'categories':categories,
        'featured_post':featured_post,
        'post':post,
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        print(f"Form is valid : {form.is_valid()}")
        if form.is_valid():
            user = form.get_user()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print("username : ", username)
            print("password : ",password)
            user = auth.authenticate(username=username, password=password)
            if(user is not None):
                auth.login(request,user)
                return redirect(to='home')
            else:
                form.add_error(None, 'Invalid username or password')
                print("Form is not valid")
                print(form.errors)
    else:
        form = AuthenticationForm()
    context = {
        'form':form 
    }
    
    return render(request, 'login.html', context)
    
def logout(request):
    auth.logout(request)
    return redirect(to='home')

# def create_post(request):
#     if request.method == "POST":
#         form = BlopPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to="home")
#     form = BlopPostForm()
#     context = {
#         'form':form,
#     }
#     return render(request,'create_post.html', context)


    