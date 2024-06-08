"""
URL configuration for crypto_scraper project.

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
from scraper import views
from django.views.generic import DetailView, ListView

urlpatterns = [
    path('', views.index, name='index'),
    path('api/taskmanager/start_scraping/', views.input_coin, name='input_coin'),
    path('api/taskmanager/scraping_status/', views.display_results, name='display_results'),
    path('api/taskmanager/scraping_status/<str:job_id>/', views.final_result, name='scraping_status'),  # Include job_id in the URL
    path('api/taskmanager/generate_job_id/', views.generate_job_id, name='generate_job_id'),  
]



