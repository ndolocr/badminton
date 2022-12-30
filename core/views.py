import os
from django.conf import settings
from pyvis.network import Network
from django.shortcuts import render
from training.models import Training

# Create your views here.

def show_pyvis_graph(request):
    network = Network(height="100vh", width="100%", bgcolor="#eeeeee" )
    
    try:
        training = Training.objects.all()
        print("All Trainings: -->", training)

        if training:
            for training_set in training:
                print("Trainer: --->", training_set.trainer)
                trainer = network.add_node(training_set.trainer.name, title='Trainer', color="#FF0")
                for trainee_set in training:
                    if trainee_set.trainer == training_set.trainer:
                        if trainee_set.training_type == "beginner":
                            trainee = network.add_node(trainee_set.trainee.name, title='Trainee')
                            training_link = network.add_edge(training_set.trainer.name, trainee_set.trainee.name, title='Trains', label="Beginner Training", color="#F00")
                        elif trainee_set.training_type == "expert":
                            trainee = network.add_node(trainee_set.trainee.name, title='Trainee')
                            training_link = network.add_edge(training_set.trainer.name, trainee_set.trainee.name, title='Trains', label="Expert Training", color="#33ff3f ")
                        elif trainee_set.training_type == "intermediate":
                            trainee = network.add_node(trainee_set.trainee.name, title='intermediate')
                            training_link = network.add_edge(training_set.trainer.name, trainee_set.trainee.name, title='Trains', label="Expert Training", color=" #335bff ")    
        network.save_graph(str(settings.BASE_DIR)+'/templates/pyvis_graph.html')
    except Exception as e:
        print(e)

    context = {}
    return render(request, "graph.html", context)