from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<species_name>/', views.detail, name='detail'),
]