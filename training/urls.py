from django.urls import path
from training.views import index, expert_training, beginner_training, intermediate_training

app_name = 'training'

urlpatterns = [
    path('', index, name='index'),
    path('/expert/training', expert_training, name='expert'),
    path('/beginner/training', beginner_training, name='beginner'),
    path('intermediate/training', intermediate_training, name='intermediate'),
]