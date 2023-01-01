from django.urls import path
from trainer import views

app_name = 'trainee'

urlpatterns = [
    path('', views.index, name='index'),
]