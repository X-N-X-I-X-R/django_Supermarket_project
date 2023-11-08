"""
URL configuration for front project.

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

from django.urls import path
from . import views 
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import views as auth_views



urlpatterns = [
    

    
    #!              ---- 2 way to create with =  views.py ----- eyal virision 

  
    path('get/category/', views.CategoryView.as_view()),
    path('get/Product/', views.ProductView.as_view()),
    path('get/Customer/new', views.CustomerCreateView.as_view()),
    path('get/Customer/order', views.OrderCreateView.as_view()),
    
    #!              ----  TOKEN  -----
    path('login/',views.MyTokenObtainPairView.as_view()),
    path("member/", views.manage_member),
    path("register/", views.manage_register),


]
