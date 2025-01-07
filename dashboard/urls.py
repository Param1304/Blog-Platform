from django.urls import path, include
from . import views 
urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/categories/', views.categories, name="categories"),
    path('dashboard/categories/add/', views.addCategory, name="add"),
    path('dashboard/posts/', views.posts, name="posts"),
    path('dashboard/posts/addpost/', views.addpost, name="addpost"),
    path('dashboard/posts/editpost/<int:pk>/', views.editpost, name="editpost"),
    path('dashboard/posts/deletepost/<int:pk>', views.deletepost,name="deletepost"),
    # path('/', include('blog_app_2.urls')),
]
