"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.CarinfoView.as_view(), name='carinfo'),
    path('apply/', views.ApplyView.as_view(), name='apply'),
    path('pickup/', views.PickupView.as_view(), name='pickup'),
]
