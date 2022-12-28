from django.conf import settings
from pyvis.network import Network
from django.shortcuts import render

# Create your views here.

def show_pyvis_graph(request):
    network = Network(height="100vh", width="100%", bgcolor="#eeeeee" )
    network.save_graph(str(settings.BASE_DIR)+'/negative_data/templates/negative_data/pyvis_graph.html')
    context = {}
    return render(request, "core/graph.html", context)