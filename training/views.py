from django.shortcuts import render
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