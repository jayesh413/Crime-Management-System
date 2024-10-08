"""CSPTS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    
# User Authentiation
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout', views.logout, name='logout'),


# Modules
    path('fir/', views.fir, name='fir'),
    path('reports/', views.reports, name='reports'),
    path('status/', views.status, name='status'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

