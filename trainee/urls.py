from django.urls import path
from trainee import views

app_name = 'trainee'

urlpatterns = [
    path('', views.index, name='index'),
]