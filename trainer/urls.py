from django.urls import path
from trainer import views

app_name = 'trainer'

urlpatterns = [
    path('', views.index, name='index'),
]