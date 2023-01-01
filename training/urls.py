from django.urls import path
from training.views import index

app_name = 'training'

urlpatterns = [
    path('', index, name='index')
]