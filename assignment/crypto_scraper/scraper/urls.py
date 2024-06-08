from django.urls import path
from .views import StartScrapingView, ScrapingStatusView, ScrapingResultsView
from . import views

urlpatterns = [
    path('api/taskmanager/scraping_status/', views.display_results, name='display_results'),
    path('api/taskmanager/scraping_status/<str:job_id>/', views.final_result, name='scraping_status'),
    path('api/taskmanager/generate_job_id/', views.generate_job_id, name='generate_job_id'),
]
