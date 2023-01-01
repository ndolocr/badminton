from django.shortcuts import render
from trainer.models import Trainer
# Create your views here.

def index(request):
    trainers = Trainer.objects.all()
    context = {"trainers": trainers}
    return render(request, 'trainer/index.html', context)