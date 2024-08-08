from django.urls import path
from .import views

urlpatterns = [
    path('', views.createPersonal, name='portfolio')
]