from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('health/', views.health_hi, name='health_hi'),
]