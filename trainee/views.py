from django.shortcuts import render
from trainee.models import Trainee
# Create your views here.

def index(request):
    trainees = Trainee.objects.all()
    context = {"trainees": trainees}
    return render(request, 'trainee/index.html', context)