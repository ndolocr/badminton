from django.shortcuts import render

from trainer.models import Trainer
from trainee.models import Trainee
from training.models import Training
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
        end_time = request.POST.get("end_time")
        start_time = request.POST.get("start_time")
        training_date = request.POST.get("training_date")

        try:
            training = Training.objects.create(
                trainee = trainee,
                trainer = trainer,
                end_time = end_time,
                start_time = start_time,
                training_type = "expert",
                training_date = training_date,
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
        trainers = Trainer.objects.filter(trailer_level = "expert")
        trainees = Trainee.objects.filter(trailer_level = "expert")

        context = {
            "trainers": trainers,
            "trainees": trainees
        }

        return render(request, 'training/add_expert_training.html', context)