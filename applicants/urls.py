from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply, name='apply'),

    # NEW API ENDPOINT
    path('api/applicants/', views.get_applicants, name='api_applicants'),
]