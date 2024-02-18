from django.urls import path
from datacenter import views

app_name = 'datacenter'


urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    #(CRUD)
    path('datacenter/<int:cable_nep>/', views.cable, name='cable'),
    path('datacenter/create/', views.create, name='create'),
    path('datacenter/<int:cable_nep>/update/', views.update, name='update'),
    path('datacenter/<int:cable_nep>/delete/', views.delete, name='delete'),

]
