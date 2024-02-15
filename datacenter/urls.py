from django.urls import path
from datacenter import views

app_name = 'datacenter'


urlpatterns = [
    path('<int:cable_nep>/', views.cable, name='cable'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
