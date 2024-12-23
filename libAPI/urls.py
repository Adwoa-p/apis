"""
URL configuration for libAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from library.views import *
from rest_framework.routers import DefaultRouter
from django.urls import re_path, path, include
from user import views


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('books/<int:id>', book_details),
    path('books/', BookViewSet.as_view({'get': 'list'}), name='book_list'),
    re_path('signup/', views.signup),
    re_path('login/', views.login),
    re_path('test_token/', views.test_token),
] + router.urls
