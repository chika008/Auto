"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from avto import views
from avto.views import blog_post
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('auto/', views.index, name='main'),
    path('auto/<int:id>/', views.details_auto, name='details_auto'),
    path('add/', blog_post, name='blog_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),  
    path('create-news/', views.create_news, name='create_news'),
    path('delete/<int:id>/', views.delete_news, name='delete_news'),
    path('update/<int:id>/', views.update_news, name='update_news'),
    path('login/', views.login_profile, name='login'),
    path('logout/', views.logout_profile, name='logout'),
    path('register/', views.register, name='register'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
