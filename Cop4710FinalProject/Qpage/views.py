from django.shortcuts import render, HttpResponse
from .models import Team, Players

def home(request):
    return render(request, 'Qpage/dota.html')

def Teams(request):
    Team_List = Teams.objects.order_by('TeamName')
    context = {'Team_List': Team_List}
    return HttpResponse("TEST")

def TeamDisplay(request, Team_Name):
    pass#PlayerList = Teams.objects.
