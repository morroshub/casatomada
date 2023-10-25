#urls de app/modulo game

from django.urls import path
from . import views
 

urlpatterns = [
    path('', views.Index),
  
]   