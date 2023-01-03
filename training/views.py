import os
from django.conf import settings
from django.shortcuts import render

from pyvis.network import Network

from trainer.models import Trainer
from trainee.models import Trainee
from training.models import Training
from facility.models import Facility
from sports_gear.models import SportsGear
# Create your views here.

def index(request):
    trainings = Training.objects.all()
    context = {
        "trainings": trainings,
        "training_type": "all",
    }

    return render(request, 'training/index.html', context)

def expert_training(request):
    trainings = Training.objects.filter(training_type = 'expert')
    context = {
        "trainings": trainings,
        "training_type": "expert",
    }

    return render(request, 'training/index.html', context)

def beginner_training(request):
    trainings = Training.objects.filter(training_type = 'beginner')
    context = {
        "trainings": trainings,
        "training_type": "begginer",
    }

    return render(request, 'training/index.html', context)

def intermediate_training(request):
    trainings = Training.objects.filter(training_type = 'intermediate')
    context = {
        "trainings": trainings,
        "training_type": "intermediate",
    }

    return render(request, 'training/index.html', context)

def add_expert_training(request):
    if request.method == 'POST':
        trainee = request.POST.get("trainee")
        trainer = request.POST.get("trainer")
        facility = request.POST.get("facility")
        training = request.POST.get("training")
        end_time = request.POST.get("end_time")
        start_time = request.POST.get("start_time")
        sportsgear = request.POST.get("sportsgear")
        training_date = request.POST.get("training_date")
        training_level = request.POST.get("training_level")

        try:
            training = Training.objects.create(
                training = training,
                end_time = end_time,
                trainee_id = trainee,
                trainer_id = trainer,
                facility_id = facility,                
                start_time = start_time,
                training_type = "expert",
                sportsgear_id = sportsgear,                              
                training_date = training_date,
                training_level = training_level,
            )
        except Exception as e:
            print("ERROR on Saving Training ", e)
        
        trainings = Training.objects.filter(training_type = 'expert')
        context = {
            "trainings": trainings,
            "training_type": "expert",
        }

        return render(request, 'training/index.html', context)
    else:
        facilities = Facility.objects.all()
        sports_gear = SportsGear.objects.all()
        trainers = Trainer.objects.filter(trailer_level = "expert")
        trainees = Trainee.objects.filter(trailer_level = "expert")

        context = {
            "trainers": trainers,
            "trainees": trainees,
            "facilities": facilities,
            "sports_gear": sports_gear,
        }

        return render(request, 'training/add_expert_training.html', context)

def add_beginner_training(request):
    if request.method == 'POST':
        print("Saving Beginner Training!")
        trainee = request.POST.get("trainee")
        trainer = request.POST.get("trainer")
        facility = request.POST.get("facility")
        training = request.POST.get("training")
        end_time = request.POST.get("end_time")
        start_time = request.POST.get("start_time")
        sportsgear = request.POST.get("sportsgear")
        training_date = request.POST.get("training_date")
        training_level = request.POST.get("training_level")

        try:
            training_record = Training.objects.create(                
                end_time = end_time,                
                training = training,
                trainee_id = trainee,
                trainer_id = trainer,
                facility_id = facility,
                start_time = start_time,
                training_type = "beginner",
                sportsgear_id = sportsgear,
                training_date = training_date,
                training_level = training_level
            )

            print("Training record, ", training_record)
        except Exception as e:
            print("ERROR on Saving Training ", e)
        
        trainings = Training.objects.filter(training_type = 'beginner')
        context = {
            "trainings": trainings,
            "training_type": "beginner",
        }

        return render(request, 'training/index.html', context)
    else:
        facilities = Facility.objects.all()
        sports_gear = SportsGear.objects.all()
        trainers = Trainer.objects.filter(trailer_level = "beginner")
        trainees = Trainee.objects.filter(trailer_level = "beginner")
        
        context = {
            "trainers": trainers,
            "trainees": trainees,
            "facilities": facilities,
            "sports_gear": sports_gear,

        }

        return render(request, 'training/add_beginner_training.html', context)

def add_intermediate_training(request):
    if request.method == 'POST':
        print("Saving Beginner Training!")
        trainee = request.POST.get("trainee")
        trainer = request.POST.get("trainer")
        facility = request.POST.get("facility")
        training = request.POST.get("training")
        end_time = request.POST.get("end_time")
        start_time = request.POST.get("start_time")
        sportsgear = request.POST.get("sportsgear")
        training_date = request.POST.get("training_date")
        training_level = request.POST.get("training_level")

        try:
            training = Training.objects.create(                
                end_time = end_time,                
                training = training,
                trainee_id = trainee,
                trainer_id = trainer,
                facility_id = facility,                
                start_time = start_time,
                sportsgear_id = sportsgear,
                training_date = training_date,
                training_type = "intermediate",
                training_level = training_level,
            )
        except Exception as e:
            print("ERROR on Saving Training ", e)
        
        trainings = Training.objects.filter(training_type = 'intermediate')
        context = {
            "trainings": trainings,
            "training_type": "intermediate",
        }

        return render(request, 'training/index.html', context)
    else:
        facilities = Facility.objects.all()
        sports_gear = SportsGear.objects.all()
        trainers = Trainer.objects.filter(trailer_level = "intermediate")
        trainees = Trainee.objects.filter(trailer_level = "intermediate")

        context = {
            "trainers": trainers,
            "trainees": trainees,
            "facilities": facilities,
            "sports_gear": sports_gear,
        }

        return render(request, 'training/add_intermediate_training.html', context)

def expert_training_graph(request):
    network = Network(height="100vh", width="100%", bgcolor="#eeeeee" )

    try:
        training_set = Training.objects.filter(training_type = "expert")

        if training_set:
            for training in training_set:
                trainer = network.add_node(training.trainer.name, title="Trainer", color=" #335bff")
                trainee = network.add_node(training.trainee.name, title="Trainee", color=" #05a414 ")
                facility = network.add_node(training.facility.name, title="Facility", color=" #a1a405 ")
                sports_gear = network.add_node(training.sportsgear.name, title="Sports gear", color="  #7b05a4 ")

                training_link = network.add_edge(training.trainer.name, training.trainee.name, title='Trains', label="Beginner Training", color="#F00")
                facility_link = network.add_edge(training.trainee.name, training.facility.name, title='Trained at', color="#F00")
                gear_link = network.add_edge(training.trainee.name, training.sportsgear.name, title='Trained at', color="#F00")
        network.save_graph(str(settings.BASE_DIR)+'/training/templates/training/expert_graph_creation.html')
    except Exception as e:
        print(e)
    
    context = {}
    return render(request, "expert_graph.html", context)

def beginner_training_graph(request):
    network = Network(height="100vh", width="100%", bgcolor="#eeeeee" )

    try:
        training_set = Training.objects.filter(training_type = "beginner")

        if training_set:
            for training in training_set:
                trainer = network.add_node(training.trainer.name, title="Trainer", color=" #335bff")
                trainee = network.add_node(training.trainee.name, title="Trainee", color=" #05a414 ")
                facility = network.add_node(training.facility.name, title="Facility", color=" #a1a405 ")
                sports_gear = network.add_node(training.sportsgear.name, title="Sports gear", color="  #7b05a4 ")

                training_link = network.add_edge(training.trainer.name, training.trainee.name, title='Trains', label="Beginner Training", color="#F00")
                facility_link = network.add_edge(training.trainee.name, training.facility.name, title='Trained at', color="#F00")
                gear_link = network.add_edge(training.trainee.name, training.sportsgear.name, title='Trained at', color="#F00")
        network.save_graph(str(settings.BASE_DIR)+'/training/templates/training/beginner_graph_creation.html')
    except Exception as e:
        print(e)
    
    context = {}
    return render(request, "beginner_graph.html", context)

def intermediate_training_graph(request):
    network = Network(height="100vh", width="100%", bgcolor="#eeeeee" )

    try:
        training_set = Training.objects.filter(training_type = "intermediate")

        if training_set:
            for training in training_set:
                trainer = network.add_node(training.trainer.name, title="Trainer", color=" #335bff")
                trainee = network.add_node(training.trainee.name, title="Trainee", color=" #05a414 ")
                facility = network.add_node(training.facility.name, title="Facility", color=" #a1a405 ")
                sports_gear = network.add_node(training.sportsgear.name, title="Sports gear", color="  #7b05a4 ")

                training_link = network.add_edge(training.trainer.name, training.trainee.name, title='Trains', label="Beginner Training", color="#F00")
                facility_link = network.add_edge(training.trainee.name, training.facility.name, title='Trained at', color="#F00")
                gear_link = network.add_edge(training.trainee.name, training.sportsgear.name, title='Trained at', color="#F00")
        network.save_graph(str(settings.BASE_DIR)+'/training/templates/training/intermediate_graph_creation.html')
    except Exception as e:
        print(e)
    
    context = {}
    return render(request, "intermediate_graph.html", context)


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