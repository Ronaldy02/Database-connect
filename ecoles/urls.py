
from django.contrib import admin
from django.urls import path
from ecole import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecole/',views.affichage),
]
