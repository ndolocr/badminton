from django.urls import path
from training.views import (index, expert_training, beginner_training, 
                            intermediate_training, add_expert_training,
                            add_beginner_training,add_intermediate_training,
                            expert_training_graph, beginner_training_graph,
                            intermediate_training_graph)

app_name = 'training'

urlpatterns = [
    path('', index, name='index'),
    path('expert/training', expert_training, name='expert'),
    path('beginner/training', beginner_training, name='beginner'),
    path('intermediate/training', intermediate_training, name='intermediate'),
    path('add_expert_training', add_expert_training, name='add_expert_training'),
    path('add_beginner_training', add_beginner_training, name='add_beginner_training'),
    path('add_intermediate_training', add_intermediate_training, name='add_intermediate_training'),
    
    path('expert_training_graph', expert_training_graph, name='expert_training_graph'),
    path('beginner_training_graph', beginner_training_graph, name='beginner_training_graph'),
    path('intermediate_training_graph', intermediate_training_graph, name='intermediate_training_graph'),
]