from django.shortcuts import render
from training.models import Training

# Create your views here.

def index(request):
    trainings = Training.objects.all()
    context = {
        "trainings": trainings,
    }

    return render(request, 'training/index.html', context)