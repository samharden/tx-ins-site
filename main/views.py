from django.shortcuts import render
from main.forms import *
# Create your views here.
def home_page(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def criminal_defense(request):
    return render(request, 'main/criminal-defense.html')

def wte_page(request):

    return render(request, 'main/wills-trusts-estates.html')

def seal_crim(request):
    return render(request, 'main/sealing-criminal-record.html')

def injunctions(request):
    return render(request, 'main/injunctions.html')

def checkup(request):
    form = mainForm()
    return render(request, 'main/legal-checkup.html', {'form':form})
