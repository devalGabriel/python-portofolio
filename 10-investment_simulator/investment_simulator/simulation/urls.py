from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('simulare/', views.simulation_form, name='simulation_form'),
    path('rezultat/', views.simulation_result, name='simulation_result'),
]
