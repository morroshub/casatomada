from django.contrib import admin
from django.urls import path, include
from game import views

 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index),
    path('', include('game.urls')), #nombre de nuestra app.urls
    path("reactpy/", include("reactpy_django.http.urls")),
]   