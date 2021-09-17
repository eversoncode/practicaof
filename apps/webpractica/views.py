from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    allmascotas = mascota.objects.all()
    allclientes = cliente.objects.all()
    allcitas = cita.objects.all()
    return render(request, 'index.html',{'allmascotas':allmascotas,'allclientes':allclientes,'allcitas':allcitas})