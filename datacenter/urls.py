from django.urls import path
from datacenter import views

app_name = 'datacenter'


urlpatterns = [
    path('', views.index, name='index'),
]
