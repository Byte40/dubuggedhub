"""
URL configuration for debugged_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', views.BlogListAPIView.as_view(), name='home'),
    path('blogs/<int:id>/', views.BlogDetailAPIView.as_view(), name='blog-detail'),
    path('blogs/topic/<int:topic_id>/', views.BlogByTopicAPIView.as_view(), name='blog-by-topic'),
    path('blogs/writer/<int:writer_id>/', views.BlogByWriterAPIView.as_view(), name='blog-by-writer'),
    path('api/blogs/', views.CreateBlogAPIView.as_view(), name='create-blog'),
    path('api/users/register/', views.UserRegistrationAPIView.as_view(), name='create-user'),
    path('api/users/login/', views.UserLoginAPIView.as_view(), name='login-user' ),
    path('api/blogs/create/', views.CreateBlogAPIView.as_view(), name='create-blog'),
]

