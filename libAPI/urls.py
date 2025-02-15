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
from library.views import *
from rest_framework.routers import DefaultRouter
from django.urls import re_path, path, include
import review.views
from user import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
# router.register(r'books', BookViewSet, basename='books') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('', include(review.urls)),
    path('books/', all_books),
    path('books/add/', book_list),
    path('books/<int:id>/', book),
    path('books/update/<int:id>', book_updates),
    # path('books/', BookViewSet.as_view({'get': 'list'}), name='book_list'),
    re_path('signup/', views.signup),
    re_path('signin/', views.signin),
    re_path('logout/', views.logout),
    re_path('test_token/', views.test_token),
    path('user/',views.user),
    path('user/reviews/',review.views.all_reviews ), 
    path('user/reviews/<int:id>',review.views.review ), 
    path('user/add_review/',review.views.add_review ), 
    path('user/reviews/<int:id>/',review.views.review_details), 
    path('user/reviews/<int:id>/<str:visibility>/', review.views.update_visibility),
    path('books/<int:id>/reviews/', review.views.book_reviews),
    path('books/<int:book_id>/reviews/<int:review_id>/', review.views.book_review)
] + router.urls
