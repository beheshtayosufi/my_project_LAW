from django.urls import path
from . import views

urlpatterns = [
    path('', views.law, name='law'),
]