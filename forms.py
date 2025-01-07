from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from blogs.models import Blogs, Category
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('email', 'username', 'password1', 'password2')
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title', 'category', 'author', 'blog_image', 'short_description', 'blog_body', 'is_featured', 'status')
