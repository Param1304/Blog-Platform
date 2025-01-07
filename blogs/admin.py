from django.contrib import admin
from . models import Category, Blogs
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','created_at','updated_at')
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','status','category','created_at','updated_at')
    prepopulated_fields = {'slug':('title',)}
    search_fields = {'id', 'title', 'author', 'category__category_name', 'status'}
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blogs)

