from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import urls 
from blogs import views as BlogsView
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name="home"),
    path('category/', include('blogs.urls')),
    path('blogs/<slug:slug>/', BlogsView.blogs, name="blogs"),
    path('register/', views.register, name = "register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # path('create_post/', views.create_post, name="create_post")
    path('', include('dashboard.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
